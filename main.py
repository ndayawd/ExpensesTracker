import os
from datetime import datetime 
import time

# Dictionary to store expense details
expenses = {"Date": [], "Category": [], "Name": [], "Amount": []}

# Function to clear the console screen based on the OS
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Clear the screen initially
clear()

# Main function to display the expense tracker menu
def main(message):
    global expenses_formatted
    expenses_formatted = []

    # Format each expense entry as a string for display
    for i in range(len(expenses["Date"])):
        formatted_string = f"Date: {str(expenses['Date'][i])} Category: {expenses['Category'][i]} Name: {expenses['Name'][i]} Amount: ${'{:.2f}'.format(expenses['Amount'][i])}"
        expenses_formatted.append(formatted_string)

    # Display menu depending on whether expenses exist
    print(f"Expense Tracker\n\nNo Expenses\n\nActions\na. Add Expenses\nb. Delete Expenses\n{message}" if expenses["Date"] == [] else f"Expense Tracker\n")

    if expenses["Date"]:  # If expenses exist, display them
        for i, items in enumerate(expenses_formatted):
            print(str(i + 1) + ":", items)
        print(f"\nTotal Expenses: ${'{:.2f}'.format(sum(expenses['Amount']))}\n\nActions\na. Add Expenses\nb. Delete Expenses\n{message}")

    # Prompt user for action selection
    action = input("Select an action (a/b): ")
    
    if action == 'a':
        clear()
        add_expenses()  # Call function to add expenses
    elif action == 'b':
        clear()
        delete_expenses("")  # Call function to delete expenses
    else:
        clear()
        main("Invalid action, please try again.")  # Handle invalid input

# Function to add expenses
def add_expenses():
    print("Expense Tracker\n")
    
    # Prompt user for expense details
    name = input("Enter a name for your expense: ")
    category = input("Enter a category for your expense: ")

    # Validate and format the amount input
    while True:
        try:
            amount = input("Enter an amount: ")
            amount_formatted = "{:.2f}".format(float(amount))
            break
        except ValueError:  # Handle invalid input
            clear()
            print("Please enter a valid number")
            time.sleep(1)
            clear()
            print(f"Expense Tracker\n\nEnter a name for your expense: {name}\nEnter a category for your expense: {category}")

    # Validate and format the date input
    while True:
        date_input = input("Enter a date (in YYYY-MM-DD format): ")
        try:
            date_object = datetime.strptime(date_input, "%Y-%m-%d")
            date = date_object.date()
            break
        except ValueError:  # Handle invalid date format
            clear()
            print("Please enter in YYYY-MM-DD format")
            time.sleep(1)
            clear()
            print(f"Expense Tracker\n\nEnter a name for your expense: {name}\nEnter a category for your expense: {category}\nEnter an amount: {amount}")

    # Append the new expense details to the dictionary
    expenses["Amount"].append(float(amount_formatted))
    expenses["Category"].append(category)
    expenses["Name"].append(name)
    expenses["Date"].append(date)

    clear()
    main("")  # Return to the main menu

# Function to delete expenses
def delete_expenses(message):
    global expenses_formatted

    if not expenses["Date"]:  # If there are no expenses, return to the main menu
        input("Expense Tracker\n\nNo Expenses\n\nPress enter to return: ")
        clear()
        main("")
    else:
        print("Expense Tracker\n")

        # Display all existing expenses
        for i, items in enumerate(expenses_formatted):
            print(str(i + 1) + ":", items)

        # List available expense indices for deletion
        numbers = '/'.join(map(str, range(1, len(expenses["Date"]) + 1)))

        # Prompt user to select an expense to delete
        delete_input = input(f"\nTotal Expenses: ${'{:.2f}'.format(sum(expenses['Amount']))}\n\n{message}\nDelete an expense ({numbers}): ")
        
        try:
            index = int(delete_input) - 1  # Convert input to index
            # Remove the selected expense from all lists
            expenses["Date"].pop(index)
            expenses["Category"].pop(index)
            expenses["Name"].pop(index)
            expenses["Amount"].pop(index)
            clear()
            main("")  # Return to the main menu
        except (ValueError, IndexError):  # Handle invalid input
            clear()
            delete_expenses("Invalid input, please try again.")

# Run the program when the script is executed
if __name__ == "__main__":
    main("")
