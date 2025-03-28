from model.new_contact_data import ContactData

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_add_new_page(self):
        wd = self.app.wd
        if  not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_xpath("//div[@id='content']/form/input[20]")) >0):
            wd.find_element_by_link_text("add new").click()

    def fill_contact_data(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname",contact.firstname)
        self.change_field_value("lastname",contact.lastname)
        self.change_field_value("address",contact.address)
        self.change_field_value("email",contact.email1)
        self.change_field_value("email2",contact.email2)
        self.change_field_value("email3",contact.email3)
        self.change_field_value("home",contact.homephone)
        self.change_field_value("mobile",contact.mobilephone)
        self.change_field_value("work",contact.workphone)
        self.change_field_value("fax",contact.fax)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def enter_add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        # select some contact
        self.select_contact_by_index(index)
        #  submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def update_first_contact(self):
        self.update_contact_by_index(0)

    def update_contact_by_index(self,index,new_contact_data):
        wd = self.app.wd
        # select first contact
        self.select_contact_by_index(index)
        # edit contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_data(new_contact_data)
        # click to update
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        return len( wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache=[]
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("id")
                lastname = element.find_element_by_xpath("//td[2]").text
                firstname = element.find_element_by_xpath("//td[3]").text
                self.contact_cache.append(ContactData(id=id,lastname=lastname,firstname=firstname  ))
        return list(self.contact_cache)