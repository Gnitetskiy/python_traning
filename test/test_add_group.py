# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.group import Group

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login( username="admin", password="secret")
    app.open_groups_page()
    app.create_group(Group(name="test 2", header="test header 2",footer="test footer 2"))
    app.return_to_groups_page()
    app.session.logout()

def test_add_empty_group(app):
    app.session.login( username="admin", password="secret")
    app.open_groups_page()
    app.create_group(Group(name="", header="",footer=""))
    app.return_to_groups_page()
    app.session.logout()



