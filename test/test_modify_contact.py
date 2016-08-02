
from model.contact import Contact

def test_modify_kontact_first_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(first_name="New Name"))
    app.session.logout()

def test_modify_kontact_last_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(last_name="New Last Name"))
    app.session.logout()