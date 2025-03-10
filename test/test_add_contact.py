# -*- coding: utf-8 -*-

from model.new_contact_data import ContactData


def test_add_contact(app):
    app.contact.open_add_new_page()
    app.contact.fill_contact_data(ContactData(firstname = "Alex", lastname = "Ivanov", address = "Mockow City", email1 = "testmail@mail.ru", email2 = "testmail2@mail.ru", email3 = "testmail3@mail.ru", homephone ="12345", mobilephone = "54321", workphone = "67890", fax = "09876"))
    app.contact.enter_add_new_contact()
    app.contact.return_to_home_page()



