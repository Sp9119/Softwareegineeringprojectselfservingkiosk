MENU_FILE = "menu.json"
#opens menu.json
with open(MENU_FILE, "r") as f:
    menu_data = json.load(f)
#instead of showing the customer hardcoded options shows the menu from menu.json
categories = ["matcha", "coffee", "tea", "snacks"]
items = {}

for category in categories:
    items[category] = list(menu_data.get(category, {}).keys())

matcha = items["matcha"]
coffee = items["coffee"]
tea = items["tea"]
snacks = items["snacks"]

# display menu
def display_menu():
    print("Welcome to Coffee Shop!")
    print("1. matcha")
    print("2. coffee")
    print("3. tea")
    print("4. snacks")
    print("5. Check out")

#display menu / ask user for selection input
def main():
    display_menu()
    option = (input("Select an menu:"))
    while option not in ["1", "2","3","4","5"]:
        print("Please enter valid menu number.")
        option = (input("Select an menu:"))

    if option == "1":
        print(matcha)
    elif option == "2":
        print(coffee)
    elif option == "3":
        print(tea)
    elif option == "4":
        print(snacks)
    elif option == "5":
        print("check out")

main()
