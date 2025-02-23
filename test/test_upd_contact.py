from model.new_contact_data import ContactData

def test_upd_first_contact(app):
    app.open_home_page_contact()
    app.session.login( username="admin", password="secret")
    app.contact.update_first_contact(ContactData(firstname = "UPD Alex", lastname = "UPD Ivanov", address = "UPD Mockow City", email1 = "UPD testmail@mail.ru", email2 = "UPD testmail2@mail.ru", email3 = "UPD testmail3@mail.ru", homephone ="UPD 12345", mobilephone = "UPD 54321", workphone = "UPD 67890", fax = "UPD 09876"))
    app.session.logout()