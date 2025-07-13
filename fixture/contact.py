from selenium.webdriver.common.by import By
from model.new_contact_data import ContactData
from selenium.webdriver.support.ui import Select
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_add_new_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements(By.XPATH, "//div[@id='content']/form/input[20]")) > 0):
            wd.find_element(By.LINK_TEXT, "add new").click()

    def fill_contact_data(self, new_contact_data):
        wd = self.app.wd
        self.change_field_value("firstname", new_contact_data.firstname)
        self.change_field_value("lastname", new_contact_data.lastname)
        self.change_field_value("address", new_contact_data.address)
        self.change_field_value("email", new_contact_data.email1)
        self.change_field_value("email2", new_contact_data.email2)
        self.change_field_value("email3", new_contact_data.email3)
        self.change_field_value("home", new_contact_data.homephone)
        self.change_field_value("mobile", new_contact_data.mobilephone)
        self.change_field_value("work", new_contact_data.workphone)
        self.change_field_value("fax", new_contact_data.fax)
        return new_contact_data

    def add_contact_in_group(self):
        wd = self.app.wd
        select = Select(wd.find_element(By.NAME, "new_group"))
        select.select_by_visible_text("name tSP")


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def enter_add_new_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "theform").click()
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value ='%s']" % id).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # select some contact
        self.select_contact_by_index(index)
        #  submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        # select some contact
        self.select_contact_by_id(id)
        #  submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        self.contact_cache = None

    def update_first_contact(self):
        self.update_contact_by_index(0)

    def update_contact_by_index(self, index, contact):
        wd = self.app.wd
        # edit contact
        wd.find_elements(By.XPATH, "//img[@alt='Edit']")[index].click()
        self.fill_contact_data(contact)
        # click to update
        wd.find_element(By.NAME, "update").click()
        self.contact_cache = None

    def update_contact_by_id(self, id, contact):
        wd = self.app.wd
        # edit contact
        wd.find_element(By.CSS_SELECTOR, 'a[href="edit.php?id=%s"]' % id).click()
        self.fill_contact_data(contact)
        # click to update
        wd.find_element(By.NAME, "update").click()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()

    def count_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for row in wd.find_elements(By.NAME, "entry"):
                cells = row.find_elements(By.TAG_NAME, "td")
                lastname = cells[1].text
                firstname = cells[2].text
                #id = cells[0].find_element(By.NAME, "selected[]").get_attribute("value")
                id = row.find_element(By.NAME, "selected[]").get_attribute("value")
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(ContactData(id=id, lastname=lastname, firstname=firstname, address=address, all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[7]
        cell.find_element(By.TAG_NAME, "a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        homephone = wd.find_element(By.NAME, "home").get_attribute("value")
        workphone = wd.find_element(By.NAME, "work").get_attribute("value")
        mobilephone = wd.find_element(By.NAME, "mobile").get_attribute("value")
        address = wd.find_element(By.NAME, "address").text
        email1 = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        return ContactData(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workphone, mobilephone=mobilephone, address=address, email1=email1, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        return ContactData(homephone=homephone, workphone=workphone, mobilephone=mobilephone)