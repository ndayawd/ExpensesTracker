import os

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

def view_expenses():

def calculate_total_expenses()

def delete_expenses()

main()