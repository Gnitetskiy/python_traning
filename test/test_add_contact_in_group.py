from model.new_contact_data import ContactData
from model.group import Group
from fixture.orm import ORMFixture

def test_add_contact_in_group(app, check_ui):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if len (db.get_group_list()) ==0:
        app.group.create_group(Group(name="name tSP"))
    group = list(filter(lambda g: g.name == "name tSP", db.get_group_list()))[0]
    old_contacts_in_group = db.get_contacts_in_group(group)
    app.contact.open_add_new_page()
    contact=app.contact.fill_contact_data(
        ContactData(firstname="Alex", lastname="Ivanov", address="Mockow City", email1="testmail@mail.ru",
                    email2="testmail2@mail.ru", email3="testmail3@mail.ru", homephone="12345", mobilephone="54321",
                    workphone="67890", fax="09876"))
    app.contact.add_contact_in_group()
    app.contact.enter_add_new_contact()
    app.contact.return_to_home_page()
    new_contacts_in_group = db.get_contacts_in_group(group)
    assert len(old_contacts_in_group) + 1 == len(new_contacts_in_group)
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=ContactData.id_or_max) == sorted(new_contacts_in_group, key=ContactData.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=ContactData.id_or_max) == sorted(app.contact.get_contact_list(), key=ContactData.id_or_max)