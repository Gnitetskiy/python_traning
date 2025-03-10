# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.create_group(Group(name="test 2", header="test header 2", footer="test footer 2"))

def test_add_empty_group(app):
    app.group.create_group(Group(name="", header="", footer=""))




