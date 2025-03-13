from model.new_contact_data import ContactData

def test_delete_first_contact(app):
    if app.contact.count_contact() ==0:
        app.contact.open_add_new_page()
        app.contact.fill_contact_data(ContactData(firstname="Alex", lastname="Ivanov", address="Mockow City", email1="testmail@mail.ru",
                        email2="testmail2@mail.ru", email3="testmail3@mail.ru", homephone="12345", mobilephone="54321",
                        workphone="67890", fax="09876"))
        app.contact.enter_add_new_contact()
    app.contact.open_contact_page()
    app.contact.delete_first_contact()
