# RPG character creator

characters = []

def welcome():
    print("*WELCOME*")
def menu():
    print("1. Create character.")
    print("2. View characters.")
    print("3. Search characters.")
    print("4. Delete character.")
    print("5. Exit.")

def create():
    name = input("Enter character's name: ")
    char_class = input("Enter character's class: ")
    level = int(input("Enter character's level: "))
    hp = int(input("Enter character's hp: "))

    characters.append({'name':name, 'class':char_class, 'level':level, 'hp':hp})
    print(f"Character named: {name} created!")
def view():
    if len(characters) == 0:
        print("You have no characters!")
        return
    print('\nYour characters:')
    for character in characters:
        print(f"{character['name']}")
        print(f"{character['class']} ")
        print(f"{character['level']} ")
        print(f"{character['hp']} ")
def search():
    user_input = input("Enter character's name: ")
    for character in characters:
        if user_input.lower() == character['name'].lower():
            print(f"{character['name']} FOUND")
            print(f"{character['class']} ")
            print(f"{character['level']} ")
            print(f"{character['hp']} ")
            return
    else:
        print(f"{user_input} NOT FOUND")
def delete():
    user_input = input("Enter character's to delete: ")
    for character in characters:
        if user_input.lower() == character['name'].lower():
            characters.remove(character)
            print(f"{character['name']} DELETED")
            return
    else:
        print(f"{user_input} NOT FOUND")

def end():
    print("Thank you for using RPG!")

welcome()

choice = 0
while choice != 5:
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        create()
    elif choice == 2:
        view()
    elif choice == 3:
        search()
    elif choice == 4:
        delete()
    elif choice == 5:
        end()
    else:
        print("invalid input!")


