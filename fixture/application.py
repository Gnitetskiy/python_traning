from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page_group(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/group.php")

    def open_home_page_contact(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/")


    def destroy (self):
        self.wd.quit()