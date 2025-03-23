from model.group import Group

def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count_group() ==0:
        app.group.create_group(Group(name="test"))
    group = Group(name="New group")
    group.id=old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0]==group



#def test_modify_group_header(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count_group() ==0:
#        app.group.create_group(Group(name="test"))
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#   assert len(old_groups) == len(new_groups)
