import os
from datetime import datetime 
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

expenses = {"Date": [], "Category": [], "Name": [], "Amount": []}  

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
        category = input("Enter a category for your expense: ")
        name = input("Enter a name for your expense: ")
        while True:
            try:
                amount = input("Enter an amount: ")
                amount = "{:.2f}".format(float(amount))
                break
            except Exception as e:
                clear()
                print(e)
                print("please enter a valid number")
                time.sleep(1)
                clear()
        while True:
            date_input = input("Enter a date (in YYYY-MM-DD format): ")
            try:
                date_object = datetime.strptime(date_input, "%Y-%m-%d")
                date = date_object.date()
                print(f"The date you entered is: {date}") 
                break
            except ValueError:
                print("Please enter in YYYY-MM-DD")
        expenses["Amount"].append(amount)
        expenses["Category"].append(category)
        expenses["Name"].append(name)
        expenses["Date"].append(date)
        print(f"{expenses}")
        user_input = input("\nPress enter to Exit: ")
        clear()
        print("Action:\n1. Add Expenses\n2. View Expenses\n3. Calculate Total Expenses\n4. Delete Expenses\n\n\n")
        main()
        
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
