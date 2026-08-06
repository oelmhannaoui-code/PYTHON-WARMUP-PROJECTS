# contact book
contacts = []

def menu():
    print('**MENU**')
    print('1. Add contact')
    print('2. Search contact')
    print('3. Delete contact')
    print('4. View contacts')
    print('5. Exit')
def add_contact():
    name = input('enter contact name :')
    phone = input('enter contact phone number :')

    contacts.append({'name':name, 'phone':phone })
    print(f'{name} added successfully')

def search_contact():
    contact_name = input('enter contact name :')
    for contact in contacts:
        if contact_name.lower() == contact['name'].lower():
            print(f'{contact["name"]} - number {contact["phone"]}')
            return
    else:
        print('contact not found')
def delete_contact():
    contact_name = input('enter contact name :')
    for contact in contacts:
        if contact_name.lower() == contact['name'].lower():
            contacts.remove(contact)
            print(f'{contact["name"]} removed successfully')
            return
    else:
        print('contact not found')
def view_contacts():
    if len(contacts) == 0:
        print('no contacts found')
        return
    print('\nyour contact list :')
    for contact in contacts:
        print(f'-{contact["name"]} - {contact["phone"]}')

def goodbye():
    print('**SEE YOU**')


print('**CONTACT MANAGER**')
choice = 0
while choice != 5:
    menu()
    choice = int(input('enter choice number :'))
    if choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        delete_contact()
    elif choice == 4:
        view_contacts()
    elif choice == 5:
        goodbye()
    else:
        print('invalid choice')
