# Employee Payroll and Deduction Analysis

name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")

basic = float(input("Enter basic pay: "))
allowances = float(input("Enter allowances: "))
hours = float(input("Enter overtime hours: "))
rate = float(input("Enter overtime rate per hour: "))
incentives = float(input("Enter incentives: "))

# Validate inputs
if (basic < 0 or allowances < 0 or
    hours < 0 or rate < 0 or incentives < 0):
    print("Invalid input! Values cannot be negative.")

else:
    # Calculate overtime pay
    overtime = hours * rate

    # Calculate gross salary
    gross = basic + allowances + overtime + incentives

    # Calculate progressive deductions
    if gross <= 10000:
        deduction = 0
    elif gross <= 20000:
        deduction = (gross - 10000) * 0.05
    else:
        deduction = 500 + (gross - 20000) * 0.10

    # Calculate net salary
    net = gross - deduction

    # Display salary statement
    print("\n========== SALARY STATEMENT ==========")
    print("Employee Name :", name)
    print("Employee ID   :", emp_id)
    print("--------------------------------------")
    print("Basic Pay     : Rs.", round(basic, 2))
    print("Allowances    : Rs.", round(allowances, 2))
    print("Overtime Pay  : Rs.", round(overtime, 2))
    print("Incentives    : Rs.", round(incentives, 2))
    print("--------------------------------------")
    print("Gross Salary  : Rs.", round(gross, 2))
    print("Deductions    : Rs.", round(deduction, 2))
    print("Net Salary    : Rs.", round(net, 2))
    print("======================================")
