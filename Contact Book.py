# Contact Book Program

# Dictionary to store contacts
contacts = {}

# Function to add a contact
def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact {name} added.")

# Function to remove a contact
def remove_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} removed.")
    else:
        print(f"Contact {name} not found.")

# Function to search for a contact
def search_contact(name):
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]}")
    else:
        print(f"Contact {name} not found.")

# Function to display all contacts
def display_contacts():
    if contacts:
        print("Contacts:")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts available.")

# Main function to run the contact book
def main():
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. Display Contacts")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            add_contact(name, phone)
        elif choice == '2':
            name = input("Enter contact name to remove: ")
            remove_contact(name)
        elif choice == '3':
            name = input("Enter contact name to search: ")
            search_contact(name)
        elif choice == '4':
            display_contacts()
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the main function
if __name__ == "__main__":
    main()
