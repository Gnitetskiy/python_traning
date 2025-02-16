# -*- coding: utf-8 -*-
import pytest
from fixture_contact import Fixture_Contact
from new_contact_data import New_Contact_Data

@pytest.fixture
def fixture_contact(request):
    fixture = Fixture_Contact()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(fixture_contact):
    fixture_contact.open_home_page()
    fixture_contact.login()
    fixture_contact.open_add_new_page()
    fixture_contact.add_new_contact(New_Contact_Data(firstname = "Alex", lastname = "Ivanov", address = "Mockow City", email1 = "testmail@mail.ru", email2 = "testmail2@mail.ru", email3 = "testmail3@mail.ru", homephone ="12345", mobilephone = "54321", workphone = "67890", fax = "09876"))
    fixture_contact.return_to_home_page()
    fixture_contact.logout()


