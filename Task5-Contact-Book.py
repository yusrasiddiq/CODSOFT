import re

# Define the contact dictionary to store contact details
contacts = {}

# Function to display all contacts
def display_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Name\t\tPhone Number\t\tEmail\t\tAddress")
        for name, details in contacts.items():
            print(f"{name}\t\t{details['phone']}\t\t{details['email']}\t\t{details['address']}")

# Function to validate phone number input
def validate_phone_number(phone):
    if phone.isdigit():
        return True
    else:
        print("Invalid phone number. Please enter digits only.")
        return False

# Function to validate email address input
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        print("Invalid email address. Please enter a valid email.")
        return False

# Main loop for the contact management system
while True:
    print("\n1. Add New Contact")
    print("2. Search Contact")
    print("3. Display Contacts")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        continue
    
    if choice == 1:
        name = input("Enter the contact name: ").lower()
        phone = input("Enter the mobile number: ")
        while not validate_phone_number(phone):
            phone = input("Enter the mobile number: ")
        email = input("Enter the email: ")
        while not validate_email(email):
            email = input("Enter the email: ")
        address = input("Enter the address: ")
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print(f"Contact for {name} added successfully.")
    
    elif choice == 2:
        search_term = input("Enter the contact name or phone number to search: ").lower()
        found = False
        for name, details in contacts.items():
            if search_term == name or search_term == details['phone']:
                print(f"Name: {name}")
                print(f"Phone: {details['phone']}")
                print(f"Email: {details['email']}")
                print(f"Address: {details['address']}")
                found = True
                break
        if not found:
            print(f"No contact found with the name or phone number {search_term}.")
    
    elif choice == 3:
        display_contacts()
    
    elif choice == 4:
        edit_name = input("Enter the name of the contact to update: ").lower()
        if edit_name in contacts:
            print("Enter new details (leave blank to keep current value):")
            phone = input(f"Current phone: {contacts[edit_name]['phone']} -> New phone: ")
            while phone and not validate_phone_number(phone):
                phone = input(f"Current phone: {contacts[edit_name]['phone']} -> New phone: ")
            phone = phone or contacts[edit_name]['phone']
            email = input(f"Current email: {contacts[edit_name]['email']} -> New email: ")
            while email and not validate_email(email):
                email = input(f"Current email: {contacts[edit_name]['email']} -> New email: ")
            email = email or contacts[edit_name]['email']
            address = input(f"Current address: {contacts[edit_name]['address']} -> New address: ") or contacts[edit_name]['address']
            contacts[edit_name] = {'phone': phone, 'email': email, 'address': address}
            print(f"Contact for {edit_name} updated successfully.")
        else:
            print(f"No contact found with the name {edit_name}.")
    
    elif choice == 5:
        del_name = input("Enter the name of the contact to delete: ").lower()
        if del_name in contacts:
            confirm = input(f"Are you sure you want to delete the contact {del_name}? (y/n): ")
            if confirm.lower() == 'y':
                del contacts[del_name]
                print(f"Contact for {del_name} deleted successfully.")
        else:
            print(f"No contact found with the name {del_name}.")
    
    elif choice == 6:
        print("Exiting the contact management system. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
