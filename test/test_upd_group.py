from model.group import Group

def test_upd_first_group(app):
    app.group.update_first_group(Group(name="upd test 3", header="upd test header 3", footer="upd test footer 3"))
