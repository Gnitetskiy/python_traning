# -*- coding: utf-8 -*-

from model.new_contact_data import ContactData


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = ContactData(firstname="Alex", lastname="Ivanov", address="Mockow City", email1="testmail@mail.ru",
                email2="testmail2@mail.ru", email3="testmail3@mail.ru", homephone="12345", mobilephone="54321",
                workphone="67890", fax="09876")
    app.contact.open_add_new_page()
    app.contact.fill_contact_data(contact)
    app.contact.enter_add_new_contact()
    app.contact.return_to_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactData.id_or_max) == sorted(new_contacts, key=ContactData.id_or_max)



