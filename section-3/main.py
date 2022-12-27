menu = """Please select one of the following options: 
 1) Add new entry
 2) View entries
 3) Exit

Your selection: """

welcome_message = "Welcome to the programming diary\n"

print(welcome_message)

while (user_selection := input(menu)) !="3":
    if user_selection == "1":
        print("You want to add a new entry")
    elif user_selection == "2":
        print("You want to view the entries")
    else:
        print("You pressed an invalid option")