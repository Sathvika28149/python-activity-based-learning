# Manufacturing Cost and Profitability Analysis

name = input("Enter product name: ")
units = int(input("Enter units produced: "))

material = float(input("Enter material cost per unit: "))
labour = float(input("Enter labour cost per unit: "))
wastage = float(input("Enter wastage percentage: "))
machine = float(input("Enter total machine cost: "))

selling = float(input("Enter selling price per unit: "))
target = float(input("Enter profit target percentage: "))

# Validate inputs
if (units <= 0 or material < 0 or labour < 0 or
    machine < 0 or selling < 0 or
    wastage < 0 or wastage > 100 or target < 0):

    print("Invalid input! Please enter valid values.")

else:
    # Calculate manufacturing costs
    material_cost = material * units
    wastage_cost = material_cost * wastage / 100
    labour_cost = labour * units

    total_cost = (
        material_cost + wastage_cost +
        labour_cost + machine
    )

    # Calculate revenue and profit
    revenue = selling * units
    profit = revenue - total_cost

    if total_cost > 0:
        profit_percentage = profit / total_cost * 100
    else:
        profit_percentage = 0

    # Display report
    print("\n--- Manufacturing Cost Report ---")
    print("Product Name:", name)
    print("Units Produced:", units)
    print("Material Cost: Rs.", round(material_cost, 2))
    print("Wastage Cost: Rs.", round(wastage_cost, 2))
    print("Labour Cost: Rs.", round(labour_cost, 2))
    print("Machine Cost: Rs.", round(machine, 2))

    print("Total Manufacturing Cost: Rs.",
          round(total_cost, 2))

    print("Total Revenue: Rs.", round(revenue, 2))
    print("Total Profit: Rs.", round(profit, 2))
    print("Profit Percentage:",
          round(profit_percentage, 2), "%")

    # Check profit target
    if profit_percentage >= target:
        print("Status: Profit target achieved.")
    else:
        print("Status: Profit target not achieved.")
