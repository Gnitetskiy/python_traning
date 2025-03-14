from model.new_contact_data import ContactData

def test_upd_first_contact(app):
    if app.contact.count_contact() ==0:
        app.contact.open_add_new_page()
        app.contact.fill_contact_data(ContactData(firstname="Alex", lastname="Ivanov", address="Mockow City", email1="testmail@mail.ru",
                        email2="testmail2@mail.ru", email3="testmail3@mail.ru", homephone="12345", mobilephone="54321",
                        workphone="67890", fax="09876"))
        app.contact.enter_add_new_contact()
    app.contact.open_contact_page()
    app.contact.update_first_contact(ContactData(firstname = "UPD Alex", lastname = "UPD Ivanov", address = "UPD Mockow City", email1 = "UPD testmail@mail.ru", email2 = "UPD testmail2@mail.ru", email3 = "UPD testmail3@mail.ru", homephone ="UPD 12345", mobilephone = "UPD 54321", workphone = "UPD 67890", fax = "UPD 09876"))
