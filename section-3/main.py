from database import add_entry, get_entries

menu = """\nPlease select one of the following options: 
 1) Add new entry
 2) View entries
 3) Exit

Your selection: """

welcome_message = "Welcome to the programming diary"

def new_entry():
    entry_content = input('What have you learned? ')
    entry_date = input("Enter date of learning: ")
    add_entry(entry_content, entry_date)
    

def view_entries(entries):
    print(f"Here are the {len(entries)} etries you asked for\n")
    for entry in entries:
        print(f"{entry['date']} - {entry['content']}")

print(welcome_message)

while (user_selection := input(menu)) !="3":
    if user_selection == "1":
        new_entry()
    
    elif user_selection == "2":        
        view_entries(get_entries())
        
    else:
        print("You pressed an invalid option")