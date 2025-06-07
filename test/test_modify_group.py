from model.group import Group
import random

def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group = Group(name="New group", id = group.id)
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups = list(map(lambda i: group if i.id == group.id else i, old_groups))
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_modify_group_header(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count_group() ==0:
#        app.group.create_group(Group(name="test"))
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#   assert len(old_groups) == len(new_groups)
