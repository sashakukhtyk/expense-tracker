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

    elif choice == 2:
        pass
    else:
        exit()