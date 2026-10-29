# Multi-Plan Telecommunications Cost Optimization

usage = float(input("Enter monthly data usage (GB): "))
calls = float(input("Enter monthly call minutes: "))
required_days = int(input("Enter required validity (days): "))
budget = float(input("Enter budget (Rs.): "))

n = int(input("Enter number of plans: "))

plans = []
eligible = []

for i in range(n):
    print("\nEnter details for Plan", i + 1)

    name = input("Enter plan name: ")
    price = float(input("Enter plan price: "))
    data = float(input("Enter included data (GB): "))
    minutes = float(input("Enter included call minutes: "))
    days = int(input("Enter validity (days): "))
    data_rate = float(input("Extra data charge per GB: "))
    call_rate = float(input("Extra call charge per minute: "))

    # Calculate excess charges
    extra_data = max(0, usage - data)
    extra_calls = max(0, calls - minutes)

    data_charge = extra_data * data_rate
    call_charge = extra_calls * call_rate

    total = price + data_charge + call_charge

    plan = {
        "name": name,
        "price": price,
        "data_charge": data_charge,
        "call_charge": call_charge,
        "total": total,
        "days": days
    }

    plans.append(plan)

    # Check eligibility
    if days >= required_days and total <= budget:
        eligible.append(plan)

# Display plan comparison
print("\n--- Mobile Plan Comparison ---")

for p in plans:
    print("\nPlan:", p["name"])
    print("Plan Price: Rs.", round(p["price"], 2))
    print("Extra Data Charges: Rs.",
          round(p["data_charge"], 2))
    print("Extra Call Charges: Rs.",
          round(p["call_charge"], 2))
    print("Total Cost: Rs.", round(p["total"], 2))
    print("Validity:", p["days"], "days")

    if p in eligible:
        print("Status: Eligible")
    else:
        print("Status: Not Eligible")

# Find the cheapest eligible plan
if eligible:
    best = min(eligible, key=lambda p: p["total"])

    print("\n--- Recommended Plan ---")
    print("Plan Name:", best["name"])
    print("Total Cost: Rs.", round(best["total"], 2))
    print("Validity:", best["days"], "days")
else:
    print("\nNo suitable plan within the given budget and validity.")
