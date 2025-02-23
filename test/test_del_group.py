
def test_delete_first_group(app):
    app.open_home_page_group()
    app.session.login( username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()