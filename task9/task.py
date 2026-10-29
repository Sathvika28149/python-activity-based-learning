# Multi-Currency Travel Budget Analysis

budget = float(input("Enter travel budget in Rs.: "))
n = int(input("Enter number of expense categories: "))

if budget < 0 or n <= 0:
    print("Invalid input!")

else:
    expenses = []
    total_spending = 0

    for i in range(n):
        print("\nExpense", i + 1)

        category = input("Enter category name: ")
        amount = float(input("Enter foreign currency amount: "))
        rate = float(input("Enter exchange rate: "))
        fee = float(input("Enter conversion fee percentage: "))

        if amount < 0 or rate <= 0 or fee < 0:
            print("Invalid expense details!")
            break

        converted = amount * rate
        conversion_fee = converted * fee / 100
        total = converted + conversion_fee

        expenses.append((category, converted,
                         conversion_fee, total))

        total_spending += total

    else:
        print("\n--- Travel Budget Report ---")

        for category, converted, fee, total in expenses:
            print("\nCategory:", category)
            print("Converted Amount: Rs.", round(converted, 2))
            print("Conversion Fee: Rs.", round(fee, 2))
            print("Total Expense: Rs.", round(total, 2))

        largest = max(expenses, key=lambda x: x[3])

        print("\nTotal Spending: Rs.", round(total_spending, 2))
        print("Travel Budget: Rs.", round(budget, 2))

        if total_spending <= budget:
            print("Remaining Budget: Rs.",
                  round(budget - total_spending, 2))
            print("Status: Within Budget")
        else:
            print("Budget Exceeded By: Rs.",
                  round(total_spending - budget, 2))
            print("Status: Over Budget")

        print("Largest Expense Category:", largest[0])
        print("Largest Expense: Rs.", round(largest[3], 2))
