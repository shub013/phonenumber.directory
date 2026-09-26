# storage.py

from directory import contacts

FILE_NAME = "contacts.txt"

def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    except FileNotFoundError:
        pass

def save_contacts():
    with open(FILE_NAME, "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")
