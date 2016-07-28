import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture




def test_kontact(app):
    app.session.login(username="admin", password="secret")
    app.contact.fillout(Contact(First_name="Alexey", last_name="Kozlov", nick="lolo", title="PM", organization="BHCC", address="250 Boston", cell="8574173906", email="alexey.kozlov@bhcc.mass.edu", birth="1988"))
    app.session.logout()

def test_2_kontact(app):
    app.session.login(username="admin", password="secret")
    app.contact.fillout(Contact(First_name="", last_name="", nick="", title="", organization="", address="", cell="", email="", birth=""))
    app.session.logout()


