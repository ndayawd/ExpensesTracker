import os
from datetime import datetime 
import time

expenses = {"Date": [], "Category": [], "Name": [], "Amount": []}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

def main(message):
    global expenses_formatted
    expenses_formatted = []
    for i in range(len(expenses["Date"])):
        formatted_string = f"Date: {str(expenses["Date"][i])} Category: {expenses["Category"][i]} Name: {expenses["Name"][i]} Amount: ${"{:.2f}".format(expenses["Amount"][i])}"
        expenses_formatted.append(formatted_string)
    print(f"Expense Tracker\n\nNo Expenses\n\nActions\na. Add Expenses\nb. Delete Expenses\n{message}" if expenses["Date"] == [] else f"Expense Tracker\n")
    if expenses["Date"] != []:
        i = 0
        for items in expenses_formatted:
            print(str(i+1) + ":", items)
            i += 1
        print(f"\nTotal Expenses: ${"{:.2f}".format(sum(expenses["Amount"]))}\n\nActions\na. Add Expenses\nb. Delete Expenses\n{message}")
    action = input("Select an action (a/b): ")
    if action == 'a':
        clear()
        add_expenses()
    elif action == 'b':
        clear()
        delete_expenses("")
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
    expenses["Amount"].append(float(amount_formatted))
    expenses["Category"].append(category)
    expenses["Name"].append(name)
    expenses["Date"].append(date)
    clear()
    main("")

def delete_expenses(message):
    global expenses_formatted
    if expenses["Date"] == []:
        input("Expense Tracker\n\nNo Expenses\n\nPress enter to return: ")
        clear()
        main("")
    else:
        print("Expense Tracker\n")
        i = 0
        for items in expenses_formatted:
            print(str(i+1) + ":", items)
            i += 1
        numbers = '/'.join(map(str, range(1, len(expenses["Date"]) + 1)))
        delete_input = input(f"\nTotal Expenses: ${"{:.2f}".format(sum(expenses["Amount"]))}\n\n{message}\nDelete an expense ({numbers}): ")
        try:
            expenses["Date"].pop(int(delete_input) - 1)
            expenses["Category"].pop(int(delete_input) - 1)
            expenses["Name"].pop(int(delete_input) - 1)
            expenses["Amount"].pop(int(delete_input) - 1)
            clear()
            main("")
        except:
            clear()
            delete_expenses("Invalid input, please try again.")

if __name__ == "__main__":
    main("")