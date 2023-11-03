class Contact:
    def __init__(self, name, phone_no, email, address):
        self.name = name
        self.phone_no = phone_no
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_no, email, address):
     
        contact = Contact(name, phone_no, email, address)
        self.contacts[name] = contact
        print(f"Contact {name} has been added successfully!")

    def view_contact(self, name):
       
        contact = self.contacts.get(name)
        if contact:
            print(f"Name: {contact.name}")
            print(f"Phone_no: {contact.phone_no}")
            print(f"Email: {contact.email}")
        else:
            print(f"Contact {name} has not found!")
        
    def search_contact(self, name):
        self.view_contact(name)
       
    def update_contact(self, name, phone_no, email):
        if name in self.contacts:
            contact = self.contacts[name]
            contact.phone_no = phone_no
            contact.email = email
            print(f"Contact {name} has been updated!")
        else:
            print(f"Contact {name} has not found!")
             
    def delete_contact(self, name):
       
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} has been deleted from the contact!")
        else:
            print(f"Contact {name}  has not found!")



def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add a Contact")
        print("2. View a Contact")
        print("3. Search for a Contact")
        print("4. Update a Contact")
        print("5. Delete a Contact")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            name = input("Enter the contact's name: ")
            phone_no = input("Enter the contact's phone number: ")
            email = input("Enter the contact's email : ")
            address = input("Enter the contact's address: ")
            contact_book.add_contact(name, phone_no, email, address)
       
        elif choice == '2':
            name = input("Enter the name of the contact to view: ")
            contact_book.view_contact(name)
        elif choice == '3':
            name = input("Enter the name to search for: ")
            contact_book.search_contact(name)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            phone_no = input("Enter the new phone number: ")
            email = input("Enter the new email address: ")
            contact_book.update_contact(name, phone_no, email)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)   
        elif choice == '6':
            print("Exiting Contact Book")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()