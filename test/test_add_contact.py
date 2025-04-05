# -*- coding: utf-8 -*-

from model.new_contact_data import ContactData
from test_add_group import random_string
import string
import pytest
import random

def random_phone(maxlen):
    return [random.choice(string.digits) for i in range(random.randrange(maxlen))]

def random_email(maxlen):
    symbols = string.ascii_letters+ string.digits +string.punctuation+ " "*10
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])+"@mail.ru"

testdata_contact = [ContactData(firstname="", lastname="", address="", email1="",
                email2="", email3="", homephone="", mobilephone="",
                workphone="", fax="")]+[
    ContactData(firstname=random_string("firstname", 5), lastname=random_string("lastname", 10), address=random_string("address", 15),email1=random_email (20),email2=random_email( 25),email3=random_email( 35),homephone=random_phone( 15),mobilephone=random_phone( 15),workphone=random_phone(15),fax=random_phone(15) )
    for i in (range(5))]


@pytest.mark.parametrize("contact", testdata_contact, ids=[repr(x) for x in testdata_contact])
def test_add_contact(app,contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.open_add_new_page()
    app.contact.fill_contact_data(contact)
    app.contact.enter_add_new_contact()
    app.contact.return_to_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactData.id_or_max) == sorted(new_contacts, key=ContactData.id_or_max)



