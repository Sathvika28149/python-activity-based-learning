# Problem Statement
To develop a Python program that evaluates multiple mobile recharge plans based on data usage, call minutes, validity period, and budget constraints. The system calculates additional charges when usage exceeds plan limits, checks which plans satisfy the user's requirements, and identifies the most economical eligible plan.
# Algorithm
1. Start the program.
2. Enter the user's monthly data usage, call minutes, required validity, and budget.
3. Enter the number of mobile plans to compare.
4. For each plan, enter its name, price, included data, included call minutes, validity, and excess usage charges.
5. Calculate additional data charges if data usage exceeds the plan limit.
6. Calculate additional call charges if call usage exceeds the plan limit.
7. Calculate the total cost of each plan using the formula:
   Total Cost = Plan Price + Excess Data Charges + Excess Call Charges
8. Check whether each plan satisfies the required validity and budget.
9. Check whether the plan provides sufficient data and call minutes, or whether excess usage can be covered within the budget.
10. Identify all eligible plans.
11. Select the eligible plan with the lowest total cost.
12. Display the cost of each plan and recommend the most economical eligible plan.
13. If no plan satisfies the requirements, display a suitable message.
14. Stop the program.
Note: The plan prices, usage limits, and excess charges used below are fictional examples for academic purposes.
# Mermaid Flowchart
Copy this code into a Mermaid editor to generate the flowchart
```flowchart TD
    A([Start]) --> B[/Enter usage, validity and budget/]
    B --> C[/Enter number of mobile plans/]
    C --> D[/Enter plan details/]
    D --> E[Calculate excess data and call charges]
    E --> F[Calculate total plan cost]
    F --> G{Validity sufficient and cost within budget?}
    G -- Yes --> H[Add plan to eligible list]
    G -- No --> I[Reject plan]
    H --> J{More plans?}
    I --> J
    J -- Yes --> D
    J -- No --> K{Any eligible plans?}
    K -- Yes --> L[Select lowest-cost eligible plan]
    K -- No --> M[Display No Suitable Plan]
```
# Input Code
This program accepts the user's requirements and the details of a mobile plan.
# Mobile Plan Input Program

usage = float(input("Enter data usage in GB: "))
calls = float(input("Enter call minutes required: "))
validity = int(input("Enter required validity in days: "))
budget = float(input("Enter budget: "))

name = input("Enter plan name: ")
price = float(input("Enter plan price: "))
data = float(input("Enter included data in GB: "))
minutes = float(input("Enter included call minutes: "))
days = int(input("Enter plan validity in days: "))

print("Plan Name:", name)
print("Plan Price:", price)
print("Included Data:", data, "GB")
print("Included Call Minutes:", minutes)
print("Validity:", days, "days")
# sample input
Enter monthly data usage (GB): 3
Enter monthly call minutes: 300
Enter required validity (days): 28
Enter budget (Rs.): 500
Enter number of plans: 3

Enter details for Plan 1
Enter plan name: Basic
Enter plan price: 199
Enter included data (GB): 2
Enter included call minutes: 200
Enter validity (days): 28
Extra data charge per GB: 50
Extra call charge per minute: 1

Enter details for Plan 2
Enter plan name: Smart
Enter plan price: 299
Enter included data (GB): 4
Enter included call minutes: 400
Enter validity (days): 56
Extra data charge per GB: 50
Extra call charge per minute: 1

Enter details for Plan 3
Enter plan name: Premium
Enter plan price: 399
Enter included data (GB): 5
Enter included call minutes: 500
Enter validity (days): 84
Extra data charge per GB: 50
Extra call charge per minute: 1
# expected output
--- Mobile Plan Comparison ---

Plan: Basic
Plan Price: Rs. 199.0
Extra Data Charges: Rs. 50.0
Extra Call Charges: Rs. 100.0
Total Cost: Rs. 349.0
Validity: 28 days
Status: Eligible

Plan: Smart
Plan Price: Rs. 299.0
Extra Data Charges: Rs. 0.0
Extra Call Charges: Rs. 0.0
Total Cost: Rs. 299.0
Validity: 56 days
Status: Eligible

Plan: Premium
Plan Price: Rs. 399.0
Extra Data Charges: Rs. 0.0
Extra Call Charges: Rs. 0.0
Total Cost: Rs. 399.0
Validity: 84 days
Status: Eligible

--- Recommended Plan ---
Plan Name: Smart
Total Cost: Rs. 299.0
Validity: 56 days
    L --> N[Display plan comparison and recommendation]
    M --> O([Stop])
    N --> O
