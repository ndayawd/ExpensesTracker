import os
from datetime import datetime 
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

expenses = {}

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
        expense_name = input("Add an Expense: ")
        expense_category = input("Enter a category for your expense: ")
        while True:
            try:
                expense_amount = int(input("Enter an amount: "))
                break
            except Exception as e:
                clear()
                print("please enter a valid number")
                time.sleep(1)
                clear()

        while True:
            date_input = input("Enter a date (in YYYY-MM-DD format): ")
            try:
                date_object = datetime.strptime(date_input, "%Y-%m-%d")
                print(f"The date you entered is: {date_object}")
                break
            except ValueError:
                print("Please enter in YYYY-MM-DD")

        expenses[expense_name] = (expense_category, expense_amount)
        print(expenses)

def view_expenses():
    print("")

def calculate_total_expenses():
    print("")

def delete_expenses():
    print("")

main()