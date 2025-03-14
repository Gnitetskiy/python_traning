class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_add_new_page(self):
        wd = self.app.wd
        if  not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_xpath("//div[@id='content']/form/input[20]")) >0):
            wd.find_element_by_link_text("add new").click()

    def fill_contact_data(self, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(new_contact_data.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(new_contact_data.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(new_contact_data.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(new_contact_data.email1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(new_contact_data.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(new_contact_data.email3)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(new_contact_data.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(new_contact_data.mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(new_contact_data.workphone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(new_contact_data.fax)

    def enter_add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        #  submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def update_first_contact(self, new_contact_data):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # edit contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_data(new_contact_data)
        # click to update
        wd.find_element_by_name("update").click()

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
