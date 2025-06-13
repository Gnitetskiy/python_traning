import re
from random import randrange
from model.new_contact_data import ContactData
# from test_phones import merge_phones_like_on_home_page, clear

#def test_all_data_on_home_page(app):
#    contacts = app.contact.get_contact_list()
#    index = randrange(len(contacts))
#    contact_from_home_page = app.contact.get_contact_list()[index]
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
#    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#    assert contact_from_home_page.address == contact_from_edit_page.address
#    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
#    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_all_contactdata_on_db(app, db):
    contacts = app.contact.get_contact_list()
    contactDB = db.get_contact_list()
    if len(contactDB) == 0:
        app.contact.open_add_new_page()
        app.contact.fill_contact_data(ContactData(firstname="Alex", lastname="Ivanov", address="Mockow City", email1="testmail@mail.ru",
                        email2="testmail2@mail.ru", email3="testmail3@mail.ru", homephone="12345", mobilephone="54321",
                        workphone="67890", fax="09876"))
        app.contact.enter_add_new_contact()
    contactDB_cleaned = []
    for contact in contactDB:
        clean_contact = ContactData(
            id=contact.id,
            firstname=contact.firstname.strip() ,
            lastname=contact.lastname.strip()
        )
        contactDB_cleaned.append(clean_contact)

    assert sorted(contacts, key=ContactData.id_or_max) == sorted(contactDB_cleaned, key=ContactData.id_or_max)

#def merge_emails_like_on_home_page(contact):
 #   return "\n".join(filter (lambda x: x != "",[contact.email1, contact.email2,contact.email3]))