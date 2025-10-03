# Phase 2 Demo Program

contacts = []  # list to store multiple contacts

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contact = [name, phone, email]  # simple list for now
    contacts.append(contact)
    print("Contact added!\n")

def view_contacts():
    if not contacts:
        print("No contacts yet.\n")
    else:
        for c in contacts:
            print("Name:", c[0], "| Phone:", c[1], "| Email:", c[2])

def menu():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

# Start program
menu()
