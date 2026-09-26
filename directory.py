# directory.py

contacts = {}

def add_contact(name, phone):
    contacts[name] = phone

def search_contact(name):
    return contacts.get(name)

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        return True
    return False

def view_contacts():
    return contacts
