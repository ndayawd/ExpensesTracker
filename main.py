import os

expenses = {}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

print("Action:\n1. Add Expenses\n2. View Expenses\n3. Calculate Total Expenses\n4. Delete Expenses\n\n\n")
def main():
    
    
    action = input("Select an action (1/2/3/4): ")
    if action == '1':
        clear()
        add_expenses()
    elif action == '2':
        clear()
        view_expenses()
    elif action == '3':
        clear()
        calculate_total_expenses()
    elif action == '4':
        clear()
        delete_expenses()
    else:
        clear()
        print("Action:\n1. Add Expenses\n2. View Expenses\n3. Calculate Total Expenses\n4. Delete Expenses\n\nInvalid action, please try again.\n")
        main()

def add_expenses():
    print("")

def view_expenses():
    if len(expenses) < 1:
        print("Expense Tracker - Current Expenses:\nNo expenses found!\n") 

        user_input = input("Press enter to Exit: ")
        if user_input.lower() == 'exit':
            clear()
            return
        else:
            clear()
            print("Action:\n1. Add Expenses\n2. View Expenses\n3. Calculate Total Expenses\n4. Delete Expenses\n\n\n")
            main()
            return

    else:
        print("Expense Tracker - Current Expenses:\n")
        print(expenses)

        user_input = input("Press enter to Exit: ")
        if user_input.lower() == 'exit':
            clear()
            return
        else:
            clear()
            print("Action:\n1. Add Expenses\n2. View Expenses\n3. Calculate Total Expenses\n4. Delete Expenses\n\n\n")
            main()
            return

def calculate_total_expenses():
    print("")

def delete_expenses():
    print("")
main()