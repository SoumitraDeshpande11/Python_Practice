expenses = []

print("Welcome to the Expense Tracker App!\n")

while True:
    print("Choose an option:")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. Calculate total expenses")
    print("4. Find the highest expense")
    print("5. Find the lowest expense")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        date = input("Enter the date (YYYY-MM-DD): ").strip()
        category = input("Enter the category (e.g., Food, Travel, Bills): ").strip()
        try:
            amount = float(input("Enter the amount spent: "))
            if amount > 0:
                expenses.append({"date": date, "category": category, "amount": amount})
                print("Expense added successfully!\n")
            else:
                print("Amount must be greater than zero. Try again.\n")
        except ValueError:
            print("Invalid input. Please enter a valid amount.\n")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet.\n")
        else:
            print("Here are all your expenses:")
            for idx, expense in enumerate(expenses, 1):
                print(f"{idx}. Date: {expense['date']}, Category: {expense['category']}, Amount: ${expense['amount']:.2f}")
            print()

    elif choice == "3":
        if not expenses:
            print("No expenses to calculate.\n")
        else:
            total = sum(expense['amount'] for expense in expenses)
            print(f"The total of all recorded expenses is: ${total:.2f}\n")

    elif choice == "4":
        if not expenses:
            print("No expenses to analyze.\n")
        else:
            highest = max(expenses, key=lambda x: x['amount'])
            print(f"The highest expense is ${highest['amount']:.2f} on {highest['date']} for {highest['category']}.\n")

    elif choice == "5":
        if not expenses:
            print("No expenses to analyze.\n")
        else:
            lowest = min(expenses, key=lambda x: x['amount'])
            print(f"The lowest expense is ${lowest['amount']:.2f} on {lowest['date']} for {lowest['category']}.\n")

    elif choice == "6":
        print("Thank you for using the Expense Tracker App. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.\n")
