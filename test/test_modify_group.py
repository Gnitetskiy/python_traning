from model.group import Group

def test_modify_group_name(app):
    if app.group.count_group() ==0:
        app.group.create_group(Group(name="test"))
    app.group.modify_first_group(Group(name="New group"))


def test_modify_group_header(app):
    if app.group.count_group() ==0:
        app.group.create_group(Group(name="test"))
    app.group.modify_first_group(Group(header="New header"))
