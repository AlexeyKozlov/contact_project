
from model.contact import Contact

def test_modify_kontact_first_name(app):
    app.contact.modify_first_contact(Contact(first_name="New Name"))

def test_modify_kontact_last_name(app):
    app.contact.modify_first_contact(Contact(last_name="New Last Name"))
