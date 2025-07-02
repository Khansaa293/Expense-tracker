expenses = []

def add_expense():
    amount = float(input("Enter expense amount: "))
    description = input("Enter description: ")
    expenses.append({"amount": amount, "description": description})
    print("Expense added.\n")

def view_total():
    total = sum(item["amount"] for item in expenses)
    print(f"Total expenses: ${total:.2f}\n")

def main():
    while True:
        print("1. Add Expense")
        print("2. View Total")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_total()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
