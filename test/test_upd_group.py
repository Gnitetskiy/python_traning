from model.group import Group

def test_upd_first_group(app):
    app.open_home_page()
    app.session.login( username="admin", password="secret")
    app.group.update_first_group(Group(name="upd test 3", header="upd test header 3", footer="upd test footer 3"))
    app.session.logout()