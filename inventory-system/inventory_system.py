# Inventory System

inventory = ["Potion", "Sword", "Shield"]


def menu():
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Use Item")
    print("4. Show Inventory")
    print("5. Exit")


def add():
    item = input("Add Item: ")
    inventory.append(item)
    print(f"{item} added!")


def remove():
    user_input = input("Remove Item: ")

    if user_input in inventory:
        inventory.remove(user_input)
        print(f"Item removed: {user_input}")
    else:
        print("Item not found.")


def use():
    user_input = input("Use Item: ")

    if user_input in inventory:
        print(f"{user_input} used.")
        inventory.remove(user_input)
    else:
        print(f"{user_input} not found.")


def show():
    print("\nYour Inventory:")

    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    for item in inventory:
        print(f"- {item}")


choice = 0

while choice != 5:
    menu()
    choice = int(input("Choose an option: "))

    if choice == 1:
        add()
    elif choice == 2:
        remove()
    elif choice == 3:
        use()
    elif choice == 4:
        show()
    elif choice == 5:
        print("Goodbye!")
    else:
        print("Invalid option.")
