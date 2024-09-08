"""
This is the main part of the program
"""
import sqlite3
import datetime


conn = sqlite3.connect('expenses.db')
cur = conn.cursor()

while True:
    print("Select an option:")
    print("1. Enter a new expense")
    print("2. View expenses summary")

    choice = int(input())

    # This is the option to add the new expense
    if choice == 1:
        # Input the date and description
        date = input("Enter the date of your expense: (YYYY-MM-DD)")
        description = input("Enter the description of your expense: ")

        # Got the categories from db
        cur.execute("SELECT DISTINCT category FROM expenses")
        categories = cur.fetchall()

        # "Select menu" of the categories
        print("Select an option by number:")
        for idx, category in enumerate(categories):
            print(f"{idx + 1}. {category[0]}")
        print(f"{len(categories) + 1} Create a new category")

        # Creating a new category
        category_choice = int(input())
        if category_choice == len(categories) + 1:
            category = input("Enter the name of the category: ")
        # Selecting a previous category
        else:
            while True:
                # Error checking part
                if category_choice < len(categories):
                    category = categories[category_choice - 1][0]
                    break
                else:
                    print("Please enter a valid category")

        # Entering the price of the expense
        price = input("Enter the price of your expense: ")

        # Storing everything into db
        cur.execute("INSERT INTO expenses (Date, description, category, price) "
                    "VALUES (?, ?, ?, ?)", (date, description, category, price))
        conn.commit()

    # This is the option to view previous expenses
    elif choice == 2:
        # Options of the view description
        print("Select an option by number:")
        print("1. View expenses summary")
        print("2. View monthly expenses by category")

        view_choice = int(input())

        if view_choice == 1:
            # View all the expenses
            cur.execute("SELECT * FROM expenses")
            expenses = cur.fetchall()
            for expense in expenses:
                print(expense)

        elif view_choice == 2:
            # View expense by month and by category
            month = input("Enter the month of your expense (MM): ")
            year = input("Enter the year of your expense (YYYY): ")
            cur.execute("SELECT category, SUM(price) FROM expenses "
                        "WHERE strftime('%m', Date) = ? AND strftime('%Y', Date) = ?"
                        "GROUP BY category", (month, year))
            expenses = cur.fetchall()

            for expense in expenses:
                print(f"Category: {expense[0]}, Total: {expense[1]}")
        else:
            exit()

    else:
        exit()