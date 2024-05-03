from utils import verify_email_address, verify_phone_number, check_name_in_contacts
from storage import read_contacts, write_contacts


CONTACT_FILE_PATH = "contacts.json"


def add_contact(contacts):
    new_contact = {}
    first_name = input("Enter first name: ").strip().lower()
    last_name = input("Enter last name: ").strip().lower()
    mobile_num = input("Enter mobile number: ").strip().lower()
    home_num = input("Enter home number: ").strip().lower()
    email = input("Enter email: ").strip().lower()
    address = input("Enter address: ").strip().lower()

    if not first_name or not last_name:
        print("You must provide a first and last name.")
    elif mobile_num and not verify_phone_number(mobile_num):
        print("Invalid number.")
    elif home_num and not verify_phone_number(home_num):
        print("Invalid number.")
    elif email and not verify_email_address(email):
        print("Invalid email.")
    elif check_name_in_contacts(first_name, last_name, contacts):
        print("That contact already exists.")
    else:
        new_contact["first_name"] = first_name
        new_contact["last_name"] = last_name
        new_contact["mobile_num"] = mobile_num
        new_contact["home_num"] = home_num
        new_contact["email"] = email
        new_contact["address"] = address

        contacts.append(new_contact)
        print("Contact successfully added!")
        return

    print("You have entered invalid information!")


def search_for_contact(contacts):
    first_name_string = input("First name: ").strip().lower()
    last_name_string = input("Last name: ").strip().lower()

    filtered_contacts = []
    for contact in contacts:
        first_name = contact["first_name"]
        last_name = contact["last_name"]

        if first_name_string and first_name_string not in first_name:
            continue
        if last_name_string and last_name_string not in last_name:
            continue

        filtered_contacts.append(contact)

    print(f"Found {len(filtered_contacts)} matching contacts.")
    list_contacts(filtered_contacts)


def list_contacts(contacts):
    ordered_contacts = sorted(contacts, key=lambda contact: contact["first_name"])
    num = 1
    for contact in ordered_contacts:
        string = f"{num}. {get_contact_string(contact)}"

        num += 1
        print(string)


def get_contact_string(contact):
    string = f"{contact['first_name'].capitalize()} {contact['last_name'].capitalize()}"

    for field in ["mobile_num", "home_num", "email", "address"]:
        value = contact[field]
        if not value:
            continue

        string += f"\n\t{field.capitalize()}: {value}"

    return string

    
def delete_contact(contacts):
    first_name = input("First name: ")
    last_name = input("Last name: ")

    contact = check_name_in_contacts(first_name, last_name, contacts)
    if not contact:
        print("No contact with that name exists.")
    else:
        warning = input(f"Are you sure you want to delete {first_name.capitalize()} {last_name.capitalize()}? (y/n): ")
        if warning == "y":
            contacts.remove(contact)
            print("Contact deleted!")


def main(contacts_path):

    message = """
    Welcome to your contact list!
    The following is a list of useable commands:      
    "add": Adds a contact.
    "delete": Deletes a contact.
    "list": Lists all contacts.
    "search": Searches for a contact by name.
    "q": Quits the program and saves the contact list.
    """

    print(message)

    contact_list = read_contacts(contacts_path)

    while True:
        
        command = input("Enter a command: ")
        
        if command == "q":
            write_contacts("contacts.json", contact_list)
            print("Contacts were saved successfully.")
            break

        elif command == "add":
            add_contact(contact_list)
        elif command == "delete":
            delete_contact(contact_list)
        elif command == "list":
            list_contacts(contact_list)
        elif command == "search":
            search_for_contact(contact_list)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main(CONTACT_FILE_PATH)