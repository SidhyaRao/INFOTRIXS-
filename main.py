
import json

def load_contacts():
    try:
        with open('contacts.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f)

def add_contact(name, phone, email):
    contacts = load_contacts()
    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)

def search_contact(name):
    contacts = load_contacts()
    found_contacts = [contact for contact in contacts if contact['name'].lower() == name.lower()]
    return found_contacts

def delete_contact(name):
    contacts = load_contacts()
    contacts = [contact for contact in contacts if contact['name'].lower() != name.lower()]
    save_contacts(contacts)

def update_contact(name, phone, email):
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contact['phone'] = phone
            contact['email'] = email
            break
    save_contacts(contacts)

def print_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Update Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            add_contact(name, phone, email)
            print("Contact added successfully.")

        elif choice == '2':
            name = input("Enter the name to search: ")
            found_contacts = search_contact(name)
            print_contacts(found_contacts)

        elif choice == '3':
            name = input("Enter the name to delete: ")
            delete_contact(name)
            print("Contact deleted successfully.")

        elif choice == '4':
            name = input("Enter the name to update: ")
            phone = input("Enter the new phone number: ")
            email = input("Enter the new email address: ")
            update_contact(name, phone, email)
            print("Contact updated successfully.")

        elif choice == '5':
            print("Exiting Contact Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

