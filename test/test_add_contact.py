
from model.contact import Contact




def test_kontact(app):
    app.contact.fillout(Contact(first_name="Alexey", last_name="Kozlov", nick="lolo", title="PM", organization="BHCC", address="250 Boston", cell="8574173906", email="alexey.kozlov@bhcc.mass.edu", birth="1988"))


def test_2_kontact(app):
    app.contact.fillout(Contact(first_name="", last_name="", nick="", title="", organization="", address="", cell="", email="", birth=""))


