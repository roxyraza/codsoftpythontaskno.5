class Contact:
    """Class to represent a contact."""
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} - {self.phone} - {self.email} - {self.address}"

class ContactBook:
    """Class to manage the contact book."""
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        """Add a new contact."""
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully.")

    def view_contacts(self):
        """View all contacts."""
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\nContact List:")
            for contact in self.contacts:
                print(contact)

    def search_contact(self, search_term):
        """Search for contacts by name or phone number."""
        results = [contact for contact in self.contacts 
                   if search_term.lower() in contact.name.lower() or 
                   search_term in contact.phone]
        if results:
            print("\nSearch Results:")
            for contact in results:
                print(contact)
        else:
            print("No contacts found.")

    def update_contact(self, name, new_details):
        """Update a contact's details."""
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone = new_details.get('phone', contact.phone)
                contact.email = new_details.get('email', contact.email)
                contact.address = new_details.get('address', contact.address)
                print(f"Contact '{contact.name}' updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        """Delete a contact."""
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            new_details = {
                'phone': phone if phone else None,
                'email': email if email else None,
                'address': address if address else None
            }
            contact_book.update_contact(name, new_details)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
