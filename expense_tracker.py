import calendar
import datetime

class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.amount}, {self.category}"

def main():
    print(f"|  Expense Tracker |")

    # Initial budget
    budget = 0

    while True:
        print("\nChoose an option:")
        print("1. Update Budget")
        print("2. Add Expense")
        print("3. Exit")
        print("")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            budget = float(input("Enter your updated budget for the month: "))
        elif choice == "2":
            # Get user input for expense.
            expense = get_user_expense()

            # Write their expense to a file.
            save_expense_to_file(expense, "expenses.csv")

            # Summarize expenses.
            summarize_expenses("expenses.csv", budget)
        elif choice == "3":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def get_user_expense():
    print("")
    print(f"| Adding Expense |")
    print("")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = [
        "Food",
        "Utilities",
        "Wellness",
        "Entertainment",
        "Misc",
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"

        try:
            selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

            if selected_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_index]
                new_expense = Expense(
                    name=expense_name, category=selected_category, amount=expense_amount
                )
                return new_expense
            else:
                print("Invalid category number. Please try again!")

        except ValueError:
            print("Invalid input. Please enter a valid category number.")

def save_expense_to_file(expense: Expense, expense_file_path):
    print("")
    print(f"| Saving User Expense: {expense} to {expense_file_path} |")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

import calendar
import datetime

class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.amount}, {self.category}"

def main():
    print(f"|  Expense Tracker |")

    # Initial budget
    budget = 0

    while True:
        print("\nChoose an option:")
        print("1. Update Budget")
        print("2. Add Expense")
        print("3. Exit")
        print("")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            budget = float(input("Enter your updated budget for the month: "))
        elif choice == "2":
            # Get user input for expense.
            expense = get_user_expense()

            # Write their expense to a file.
            save_expense_to_file(expense, "expenses.csv")

            # Summarize expenses.
            summarize_expenses("expenses.csv", budget)
        elif choice == "3":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def get_user_expense():
    print("")
    print(f"| Adding Expense |")
    print("")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = [
        "Food",
        "Utilities",
        "Wellness",
        "Entertainment",
        "Misc",
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"

        try:
            selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

            if selected_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_index]
                new_expense = Expense(
                    name=expense_name, category=selected_category, amount=expense_amount
                )
                return new_expense
            else:
                print("Invalid category number. Please try again!")

        except ValueError:
            print("Invalid input. Please enter a valid category number.")

def save_expense_to_file(expense: Expense, expense_file_path):
    print("")
    print(f"| Saving User Expense: {expense} to {expense_file_path} |")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expenses(expense_file_path, original_budget):
    print("")
    print(f"| Summarizing User Expense |")
    print("")
    expenses: list[Expense] = []

    try:
        with open(expense_file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                # Check if the line is not empty
                if line.strip():
                    # Check if the line has the expected format
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        expense_name, expense_amount, expense_category = parts
                        line_expense = Expense(
                            name=expense_name,
                            amount=float(expense_amount),
                            category=expense_category,
                        )
                        expenses.append(line_expense)
                    else:
                        print(f"Skipping invalid line: {line}")

        amount_by_category = {}
        for expense in expenses:
            key = expense.category
            if key in amount_by_category:
                amount_by_category[key] += expense.amount
            else:
                amount_by_category[key] = expense.amount

        print("Expenses By Category :")
        for key, amount in amount_by_category.items():
            print(f"  {key}: ${amount:.2f}")
        print("")
        print(f"Total Spent: ${sum([x.amount for x in expenses]):.2f}")
        print(f"Original Budget: ${original_budget:.2f}")

        remaining_budget = original_budget - sum([x.amount for x in expenses])
        print(f"Budget Remaining: ${remaining_budget:.2f}")

        now = datetime.datetime.now()
        days_in_month = calendar.monthrange(now.year, now.month)[1]
        remaining_days = days_in_month - now.day

        if remaining_days > 0:
            daily_budget = remaining_budget / remaining_days
            print(f"👉 Budget Per Day: ${daily_budget:.2f}")
        else:
            print("The month has ended. Budget per day cannot be calculated.")

    except FileNotFoundError:
        print(f"File '{expense_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def green(text):
    return f"\033[92m{text}\033[0m"

if __name__ == "__main__":
    main()
