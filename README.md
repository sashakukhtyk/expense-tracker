# Expense Tracker

This is a simple Python-based expense tracking program that allows users to log and view their expenses. It uses an SQLite database (`expenses.db`) to store the records of expenses with categories, descriptions, dates, and amounts.

## Features

- **Add new expenses**: Users can enter new expenses with a date, description, category, and price.
- **View expenses summary**: Users can view a summary of all expenses or filter expenses by category and month.
- **Category management**: Users can select an existing category or create a new one when adding an expense.

## Requirements

- Python 3.x
- SQLite3 (pre-installed with Python)

## Setup

1. Clone this repository or download the `expenses.py` file.
2. Make sure Python is installed on your system. If not, [download and install Python](https://www.python.org/downloads/).
3. Create an SQLite database (`expenses.db`) with the following structure:

```sql
CREATE TABLE expenses (
    Date TEXT,
    description TEXT,
    category TEXT,
    price REAL
);
```
4. Run the Python script using the following command:

```bash
python expenses.py
```
## Usage

Upon running the program, you will be presented with two main options:

### 1. Enter a New Expense

- The program will ask for the date of the expense (in `YYYY-MM-DD` format), the description, and the price.
- You can choose an existing category for the expense or create a new category.

### 2. View Expenses Summary

- **View all expenses**: Displays all recorded expenses.
- **View monthly expenses by category**: Allows you to enter a specific month and year to view a summary of expenses grouped by category.

After performing an action, the program will ask if you want to continue or exit.

## Example

```bash
Select an option:
1. Enter a new expense
2. View expenses summary
1
Enter the date of your expense: (YYYY-MM-DD) 2024-08-10
Enter the description of your expense: Groceries
Select an option by number:
1. Food
2. Transportation
3. Create a new category
3
Enter the name of the category: Groceries
Enter the price of your expense: 50.00
```
## License

This project is licensed under the MIT License. See the LICENSE file for details.
