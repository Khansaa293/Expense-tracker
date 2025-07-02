expenses = []

def add_expense():
    amount = float(input("Enter expense amount: "))
    description = input("Enter description: ")
    expenses.append({"amount": amount, "description": description})
    print("Expense added.\n")

def view_total():
    total = sum(item["amount"] for item in expenses)
    print(f"Total expenses: ${total:.2f}\n")

def delete_expense():
    if not expenses:
        print("No expenses to delete.\n")
        return

    for idx, expense in enumerate(expenses):
        print(f"{idx + 1}. {expense['description']} - ${expense['amount']:.2f}")
    try:
        choice = int(input("Enter the number of the expense to delete: "))
        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)
            print(f"Deleted: {removed['description']} - ${removed['amount']:.2f}\n")
        else:
            print("Invalid choice.\n")
    except ValueError:
        print("Invalid input.\n")

def main():
    while True:
        print("1. Add Expense")
        print("2. View Total")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_total()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
