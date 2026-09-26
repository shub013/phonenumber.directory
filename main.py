from directory import add_contact, search_contact, delete_contact, view_contacts
from storage import load_contacts, save_contacts

load_contacts()

while True:
    print("\n===== PHONE DIRECTORY =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View All Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        add_contact(name, phone)
        save_contacts()
        print("Contact saved successfully!")

    elif choice == "2":
        name = input("Enter name: ")
        result = search_contact(name)
        if result:
            print(f"{name} : {result}")
        else:
            print("Contact not found.")

    elif choice == "3":
        data = view_contacts()
        if len(data) == 0:
            print("No contacts available.")
        else:
            print("\n--- Contact List ---")
            for name, phone in data.items():
                print(f"{name} : {phone}")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if delete_contact(name):
            save_contacts()
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Thank you for using Phone Directory!")
        break

    else:
        print("Invalid choice. Try again.")
