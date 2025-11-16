import json
import subprocess

MENU_FILE = "menu.json"

with open(MENU_FILE, "a+") as f:
    f.seek(0)
    content = f.read()
    if not content:
        f.write("{}")

class Administrator:
    def __init__(self):
        with open(MENU_FILE, "r") as f:
            self.menu = json.load(f)

    def save_menu(self):
        with open(MENU_FILE, "w") as f:
            json.dump(self.menu, f, indent=4)

    def add_item(self, category, item, price):
        if category not in self.menu:
            self.menu[category] = {}
        if item in self.menu[category]:
            print(f"Item '{item}' already exists in category '{category}'.")
        else:
            self.menu[category][item] = price
            print(f"Item '{item}' added to '{category}' with price {price}!")
            self.save_menu()

    def remove_item(self, category, item):
        if category not in self.menu:
            print(f"Category '{category}' does not exist.")
            return
        if item not in self.menu[category]:
            print(f"Item '{item}' does not exist in category '{category}'.")
            return
        del self.menu[category][item]
        print(f"Item '{item}' removed from category '{category}'.")
        # If the category is empty now, remove it
        if not self.menu[category]:
            del self.menu[category]
        self.save_menu()

    def change_price(self, category, item, price):
        if category not in self.menu:
            print(f"Category '{category}' does not exist.")
            return
        if item not in self.menu[category]:
            print(f"Item '{item}' does not exist in category '{category}'.")
            return
        self.menu[category][item] = price
        print(f"Price of '{item}' in category '{category}' changed to {price}!")
        self.save_menu()

def administer():
    admin = Administrator()
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Change Price")
        print("4. Exit")

        option = input("Select an option: ")
        while option not in ["1", "2", "3", "4"]:
            print("Please enter a valid option.")
            option = input("Select an option: ")

        if option == "1":
            category = input("Enter category: ")
            item = input("Enter item name: ")
            price = float(input("Enter price: "))
            admin.add_item(category, item, price)

        elif option == "2":
            category = input("Enter category: ")
            item = input("Enter item name: ")
            admin.remove_item(category, item)

        elif option == "3":
            category = input("Enter category: ")
            item = input("Enter item name: ")
            price = float(input("Enter new price: "))
            admin.change_price(category, item, price)

#going to use subprocess to return user to login page
        elif option == "4":
            print("Returning to login page...")
            subprocess.run(["python3", "Login.py"])
            break

administer()

