# Problem Statement

Develop a Python program to analyze a travel budget when expenses are made in different currencies. The program accepts expense categories, amounts, exchange rates, conversion fees, and the total budget. It converts all expenses into the home currency, calculates the total spending, checks whether the budget is exceeded, and identifies the largest expense category.

# Algorithm

Start the program.

Enter the total travel budget in the home currency.

Enter the number of expense categories.

For each category, enter:

Expense category name.

Expense amount in foreign currency.

Exchange rate to the home currency.

Currency conversion fee percentage.

Calculate the converted expense:

Converted amount = Foreign amount × Exchange rate.

Calculate the conversion fee:

Conversion fee = Converted amount × Fee percentage / 100.

Calculate the total expense:

Total expense = Converted amount + Conversion fee.

Add all expenses to calculate total spending.

Compare total spending with the travel budget.

Identify the category with the highest total expense.

Display the converted expenses, fees, total spending, remaining budget or excess amount, and largest expense category.

Stop the program.

# Mermaid Flowchart
```flowchart TD
    A([Start]) --> B[/Enter travel budget/]
    B --> C[/Enter number of expense categories/]
    C --> D[/Enter category, amount, exchange rate and fee/]
    D --> E[Convert amount to home currency]
    E --> F[Calculate conversion fee]
    F --> G[Calculate total category expense]
    G --> H[Add expense to total spending]
    H --> I{More categories?}
    I -- Yes --> D
    I -- No --> J[Find largest expense category]
    J --> K{Spending within budget?}
    K -- Yes --> L[Calculate remaining budget]
    K -- No --> M[Calculate excess spending]
    L --> N[Display final report]
    M --> N
    N --> O([Stop])
```
4. Input Code

This code accepts and displays the travel expense details.

# Multi-Currency Travel Budget Input

budget = float(input("Enter travel budget in Rs.: "))
n = int(input("Enter number of expense categories: "))

for i in range(n):
    print("\nExpense", i + 1)

    category = input("Enter category name: ")
    amount = float(input("Enter foreign currency amount: "))
    rate = float(input("Enter exchange rate: "))
    fee = float(input("Enter conversion fee percentage: "))

    print("Category:", category)
# Sample Input

For this example, the home currency is Indian Rupees (INR). The exchange rates and fees below are illustrative values.

Enter travel budget in Rs.: 50000
Enter number of expense categories: 3

Expense 1
Enter category name: Hotel
Enter foreign currency amount: 200
Enter exchange rate: 85
Enter conversion fee percentage: 2

Expense 2
Enter category name: Food
Enter foreign currency amount: 100
Enter exchange rate: 85
Enter conversion fee percentage: 1

Expense 3
Enter category name: Shopping
Enter foreign currency amount: 300
Enter exchange rate: 85
Enter conversion fee percentage: 2

# Sample Output

--- Travel Budget Report ---

Category: Hotel
Converted Amount: Rs. 17000.0
Conversion Fee: Rs. 340.0
Total Expense: Rs. 17340.0

Category: Food
Converted Amount: Rs. 8500.0
Conversion Fee: Rs. 85.0
Total Expense: Rs. 8585.0

Category: Shopping
Converted Amount: Rs. 25500.0
Conversion Fee: Rs. 510.0
Total Expense: Rs. 26010.0

Total Spending: Rs. 51935.0
Travel Budget: Rs. 50000.0
Budget Exceeded By: Rs. 1935.0
Status: Over Budget
Largest Expense Category: Shopping

    print("Foreign Amount:", amount)
    print("Exchange Rate:", rate)
    print("Conversion Fee:", fee, "%")
