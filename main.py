
def add_contacts(name, phone, email, contacts_list):
    new_contact = {'name': name, 'phone': phone, 'email': email}
    contacts_list.append(new_contact)

def search_contact(name, contacts_list):
    found_contacts = []
    for contact in contacts_list:
        if contact['name'] == name:
            found_contacts.append(contact)
    return found_contacts

def delete_contact(name, contacts_list):
    for contact in contacts_list:
        if contact['name'] == name:
            contacts_list.remove(contact)

def update_contact(name, phone, email, contacts_list):
    for contact in contacts_list:
        if contact['name'] == name:
            contact['phone'] = phone
            contact['email'] = email

def main():
    contacts = []  # Initialize an empty list to store contacts
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
            add_contacts(name, phone, email, contacts)
            print("Contact added successfully.")

        elif choice == '2':
            name = input("Enter the name to search: ")
            found_contacts = search_contact(name, contacts)
            print_contacts(found_contacts)

        elif choice == '3':
            name = input("Enter the name to delete: ")
            delete_contact(name, contacts)
            print("Contact deleted successfully.")

        elif choice == '4':
            name = input("Enter the name to update: ")
            phone = input("Enter the new phone number: ")
            email = input("Enter the new email address: ")
            update_contact(name, phone, email, contacts)
            print("Contact updated successfully.")

        elif choice == '5':
            print("Exiting Contact Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

def print_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

if __name__ == "__main__":
    main()
