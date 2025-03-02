# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.new_contact_data import ContactData

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.open_home_page()
    app.session.login( username="admin", password="secret")
    app.contact.open_add_new_page()
    app.contact.add_new_contact(ContactData(firstname = "Alex", lastname = "Ivanov", address = "Mockow City", email1 = "testmail@mail.ru", email2 = "testmail2@mail.ru", email3 = "testmail3@mail.ru", homephone ="12345", mobilephone = "54321", workphone = "67890", fax = "09876"))
    app.contact.enter_add_new_contact()
    app.contact.return_to_home_page()
    app.session.logout()


