import os
from datetime import datetime 
import time

expenses = {"Date": [], "Category": [], "Name": [], "Amount": []}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

def main(message):
    expenses_formatted = []
    for i in range(len(expenses["Date"])):
        formatted_string = f"Date: {str(expenses["Date"][i-1])} Category: {expenses["Category"][i-1]} Name: {expenses["Name"][i-1]} Amount: ${expenses["Amount"][i-1]}"
        expenses_formatted.append(formatted_string)
    print(f"Expense Tracker\n\nNo Expenses\n\nActions\n1. Add Expenses\n2. Delete Expenses\n{message}" if expenses["Date"] == [] else f"Expense Tracker\n\n")
    if expenses["Date"] != []:
        i = 0
        for items in expenses_formatted:
            print(str(i+1) + ":", items)
            i += 1
        print(f"\n\nActions\n1. Add Expenses\n2. Delete Expenses\n{message}")
    action = input("Select an action (1/2): ")
    if action == '1':
        clear()
        add_expenses()
    elif action == '2':
        clear()
        delete_expenses()
    else:
        clear()
        main("Invalid action, please try again.")

def add_expenses():
    print("Expense Tracker\n")
    name = input("Enter a name for your expense: ")
    category = input("Enter a category for your expense: ")
    while True:
        try:
            amount = input("Enter an amount: ")
            amount_formatted = "{:.2f}".format(float(amount))
            break
        except:
            clear()
            print("Please enter a valid number")
            time.sleep(1)
            clear()
            print(f"Expense Tracker\n\nEnter a name for your expense: {name}\nEnter a category for your expense: {category}")
    while True:
        date_input = input("Enter a date (in YYYY-MM-DD format): ")
        try:
            date_object = datetime.strptime(date_input, "%Y-%m-%d")
            date = date_object.date()
            break
        except:
            clear()
            print("Please enter in YYYY-MM-DD format")
            time.sleep(1)
            clear()
            print(f"Expense Tracker\n\nEnter a name for your expense: {name}\nEnter a category for your expense: {category}\nEnter an amount: {amount}")
    expenses["Amount"].append(amount_formatted)
    expenses["Category"].append(category)
    expenses["Name"].append(name)
    expenses["Date"].append(date)
    print(f"\nExpense added")
    clear()
    main("")

def delete_expenses():
    print("")0

main("")
