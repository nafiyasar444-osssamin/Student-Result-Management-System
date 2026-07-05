expenses = []

def save_expenses():
    with open("expenses.txt", "w") as file:
        for item in expenses:
            file.write(f"{item[0]},{item[1]}\n")

def load_expenses():
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                name, amount = line.strip().split(",")
                expenses.append((name, float(amount)))
    except FileNotFoundError:
        pass

load_expenses()

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        name = input("Expense Name: ")
        amount = float(input("Amount: "))
        expenses.append((name, amount))
        save_expenses()
        print("Expense Added Successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No Expense Found")
        else:
            print("\nExpense\tAmount")
            for item in expenses:
                print(item[0], "\t", item[1])

    elif choice == "3":
        total = 0
        for item in expenses:
            total += item[1]
        print("Total Expense =", total)

    elif choice == "4":
        print("Good Bye!")
        break

    else:
        print("Invalid Choice")
