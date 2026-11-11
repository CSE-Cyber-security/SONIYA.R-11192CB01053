expenses = []

while True:
    print("\n===== DAILY EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expenses.append([name, amount])
        print("Expense added successfully!")

    elif choice == 2:
        print("\nYour Expenses:")
        for expense in expenses:
            print(expense[0], "-", expense[1])

    elif choice == 3:
        total = sum(expense[1] for expense in expenses)
        print("Total Expenses: Rs.", total)

    elif choice == 4:
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")
