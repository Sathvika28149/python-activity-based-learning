# Problem Statement
To develop a Python program that calculates the total manufacturing cost of products using material costs, labour charges, wastage costs, and machine costs. The system calculates the selling price, determines the profit earned per product, and checks whether the production meets a specified profit target.
# Algorithm
1. Start the program.
2. Enter the product name and number of units produced.
3. Enter the material cost per unit, labour cost per unit, wastage percentage, and total machine cost.
4. Enter the selling price per unit and the required profit target percentage.
5. Validate all inputs to ensure they are non-negative and the wastage percentage is within a valid range.
6. Calculate the total material cost.
7. Calculate the wastage cost based on the material cost.
8. Calculate the total labour cost.
9. Add the machine cost to obtain the total manufacturing cost.
10. Calculate the total revenue using selling price per unit × units produced.
11. Calculate profit using total revenue − total manufacturing cost.
12. Calculate the profit percentage based on the total manufacturing cost.
13. Compare the profit percentage with the required profit target.
14. Display the total manufacturing cost, revenue, profit, profit percentage, and target status.
15. Stop the program.
Note: The cost values and profit targets are illustrative examples for this academic project.
# Mermaid Flowchart
Copy this code into a Mermaid editor to generate the flowchart.
```flowchart TD
    A([Start]) --> B[/Enter product details and costs/]
    B --> C{Are inputs valid?}
    C -- No --> D[Display Invalid Input]
    D --> Z([Stop])
    C -- Yes --> E[Calculate Material Cost]
    E --> F[Calculate Wastage Cost]
    F --> G[Calculate Labour Cost]
    G --> H[Calculate Total Manufacturing Cost]
    H --> I[Calculate Total Revenue]
    I --> J[Calculate Profit and Profit Percentage]
    J --> K{Profit Percentage >= Target?}
    K -- Yes --> L[Production Meets Profit Target]
    K -- No --> M[Production Does Not Meet Target]
    L --> N[Display Cost and Profit Report]
    M --> N
    N --> Z
```
# Input Code
This program accepts the product details and manufacturing costs.
# Manufacturing Cost Input Program

name = input("Enter product name: ")
units = int(input("Enter units produced: "))

material = float(input("Enter material cost per unit: "))
labour = float(input("Enter labour cost per unit: "))
wastage = float(input("Enter wastage percentage: "))
machine = float(input("Enter total machine cost: "))

selling = float(input("Enter selling price per unit: "))
target = float(input("Enter profit target percentage: "))

print("Product Name:", name)
print("Units Produced:", units)
print("Material Cost:", material)
print("Labour Cost:", labour)
print("Wastage Percentage:", wastage)
print("Machine Cost:", machine)
print("Selling Price:", selling)
print("Profit Target:", target)
# sample input
Enter product name: Chair
Enter units produced: 100
Enter material cost per unit: 200
Enter labour cost per unit: 50
Enter wastage percentage: 5
Enter total machine cost: 2000
Enter selling price per unit: 350
Enter profit target percentage: 15
# expected output
--- Manufacturing Cost Report ---
Product Name: Chair
Units Produced: 100
Material Cost: Rs. 20000.0
Wastage Cost: Rs. 1000.0
Labour Cost: Rs. 5000.0
Machine Cost: Rs. 2000.0
Total Manufacturing Cost: Rs. 28000.0
Total Revenue: Rs. 35000.0
Total Profit: Rs. 7000.0
Profit Percentage: 25.0 %
Status: Profit target achieved.
