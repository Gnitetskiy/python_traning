# -*- coding: utf-8 -*-

from model.new_contact_data import ContactData


def test_add_contact(app,db,json_contacts):
    contact=json_contacts
    old_contacts = db.get_contact_list()
    app.contact.open_add_new_page()
    app.contact.fill_contact_data(contact)
    app.contact.enter_add_new_contact()
    app.contact.return_to_home_page()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactData.id_or_max) == sorted(new_contacts, key=ContactData.id_or_max)



