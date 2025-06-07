from model.new_contact_data import ContactData
import random

def test_upd_first_contact(app, db,check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.open_add_new_page()
        app.contact.fill_contact_data(ContactData(firstname="Alex", lastname="Ivanov", address="Mockow City", email1="testmail@mail.ru",
                        email2="testmail2@mail.ru", email3="testmail3@mail.ru", homephone="12345", mobilephone="54321",
                        workphone="67890", fax="09876"))
        app.contact.enter_add_new_contact()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact= ContactData(firstname="UPD Alex", lastname="UPD Ivanov", id= contact.id)
    app.contact.update_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts= list(map(lambda i: contact if i.id == contact.id else i, old_contacts ))
    assert sorted(old_contacts, key=ContactData.id_or_max) == sorted(new_contacts, key=ContactData.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=ContactData.id_or_max) == sorted(app.contact.get_contact_list(), key=ContactData.id_or_max)

