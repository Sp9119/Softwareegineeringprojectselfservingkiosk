def display_login():
    print("Welcome please pick an option")
    print("1. Menu")
    print("2. Administer")

def main():
    display_login()
    option = (input("Select an option:"))
    while option not in ["1", "2"]:
        print("Please enter valid option.")
        option = (input("option:"))

    if option == "1":
        import Menu
        menu.show_Menu()
    elif option == "2":
        import Administer
        Administer.admin_panel()

if __name__ == "__main__":
    main()
