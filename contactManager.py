import json


def load_contacts():
    try:
        with open("contacts.json",'r') as contacts:
            data=json.load(contacts)

        return data
    except(FileNotFoundError, json.JSONDecodeError):
        print("Error: Could not load contacts. Starting with an empty list.")
        return []

def add_contact():
    name = input("Insert your name: ")
    email = input("Insert your email: ")
    phone = input("Insert your phone: ")

    contactsData = load_contacts()  #load current state of contacts

    newContact = {
        "name": name,
        "email": email,
        "phone": phone
    }

    contactsData.append(newContact)

    with open("contacts.json",'w') as contactsFile:
        json.dump(contactsData, contactsFile, indent=4)

    print("Contact added successfully")

def view_contacts():
    contacts = load_contacts()

    if len(contacts) == 0:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}")


def main_menu():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add a contact")
        print("2. View contacts")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_contact()  # Call add_contact function
        elif choice == '2':
            view_contacts()  # Call view_contacts function
        elif choice == '3':
            print("Exiting the program.")
            break  # Exit the loop to stop the program
        else:
            print("Invalid choice. Please try again.")


#call main menu to start the program
#the point where all triggered
main_menu()





