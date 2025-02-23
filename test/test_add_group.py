# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.open_home_page_group()
    app.session.login( username="admin", password="secret")
    app.group.create_group(Group(name="test 2", header="test header 2", footer="test footer 2"))
    app.session.logout()

def test_add_empty_group(app):
    app.open_home_page_group()
    app.session.login( username="admin", password="secret")
    app.group.create_group(Group(name="", header="", footer=""))
    app.session.logout()



