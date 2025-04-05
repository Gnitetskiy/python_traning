from model.new_contact_data import ContactData
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_add_new_page(self):
        wd = self.app.wd
        if  not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_xpath("//div[@id='content']/form/input[20]")) >0):
            wd.find_element_by_link_text("add new").click()

    def fill_contact_data(self, new_contact_data):
        wd = self.app.wd
        self.change_field_value("firstname",new_contact_data.firstname)
        self.change_field_value("lastname",new_contact_data.lastname)
        self.change_field_value("address",new_contact_data.address)
        self.change_field_value("email",new_contact_data.email1)
        self.change_field_value("email2",new_contact_data.email2)
        self.change_field_value("email3",new_contact_data.email3)
        self.change_field_value("home",new_contact_data.homephone)
        self.change_field_value("mobile",new_contact_data.mobilephone)
        self.change_field_value("work",new_contact_data.workphone)
        self.change_field_value("fax",new_contact_data.fax)


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

    def update_contact_by_index(self,index,contact):
        wd = self.app.wd
        # edit contact
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_data(contact)
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
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(ContactData(id=id,lastname=lastname,firstname=firstname,address=address,all_emails_from_home_page=all_emails,all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self,index):
        wd = self.app.wd
        self.app.open_home_page()
        row=wd.find_elements_by_name("entry")[index]
        cell=row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self,index):
        wd = self.app.wd
        self.app.open_home_page()
        row=wd.find_elements_by_name("entry")[index]
        cell=row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self,index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone =wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email1= wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return ContactData(firstname=firstname, lastname=lastname, id=id, homephone=homephone,workphone=workphone,mobilephone=mobilephone,address=address,email1=email1,email2=email2,email3=email3)

    def get_contact_from_view_page(self,index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text=wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)",text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        return ContactData(homephone=homephone,workphone=workphone,mobilephone=mobilephone)

