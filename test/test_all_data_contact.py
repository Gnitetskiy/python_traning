import re
from random import randrange
from model.new_contact_data import ContactData
from test.test_phones import merge_phones_like_on_home_page, clear

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
    contactUI = sorted(app.contact.get_contact_list(), key=ContactData.id_or_max)
    contactDB = sorted(db.get_contact_list(), key=ContactData.id_or_max)
    for i in range(len(contactUI)):
        contact_ui = contactUI[i]
        contact_db = contactDB[i]
        assert clear_(contact_ui.firstname) == clear_(contact_db.firstname)
        assert clear_(contact_ui.lastname) == clear_(contact_db.lastname)
        assert clear_(contact_ui.address) == clear_(contact_db.address)
        assert clear_(contact_ui.all_emails_from_home_page) == merge_emails_like_on_home_page(contact_db)
        assert contact_ui.all_phones_from_home_page == merge_phones_like_on_home_page(contact_db)


def merge_emails_like_on_home_page(contact):
    return "\n".join(map(lambda x: clear_(x),
        filter (lambda x: x is not None and x != "",
                             [contact.email1, contact.email2,contact.email3])))


def clear_(s):
    return re.sub(" ", "", s)

