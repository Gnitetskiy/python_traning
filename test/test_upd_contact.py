from model.new_contact_data import ContactData
from random import randrange

def test_upd_first_contact(app):
    if app.contact.count_contact() ==0:
        app.contact.open_add_new_page()
        app.contact.fill_contact_data(ContactData(firstname="Alex", lastname="Ivanov", address="Mockow City", email1="testmail@mail.ru",
                        email2="testmail2@mail.ru", email3="testmail3@mail.ru", homephone="12345", mobilephone="54321",
                        workphone="67890", fax="09876"))
        app.contact.enter_add_new_contact()
    app.contact.open_contact_page()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact= ContactData(firstname = "UPD Alex", lastname = "UPD Ivanov")
    contact.id = old_contacts [index].id
    app.contact.update_contact_by_index(index,contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index]= contact
    assert sorted(old_contacts, key=ContactData.id_or_max) == sorted(new_contacts, key=ContactData.id_or_max)

