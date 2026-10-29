# Problem Statement
To develop a Python program that calculates an employee's gross salary using basic pay, allowances, overtime, and incentives. The system applies progressive deductions based on salary slabs, calculates the net salary, and generates a formatted salary statement showing earnings, deductions, and the final amount payable to the employee.
# Algorithm
1. Start the program.
2. Enter the employee's name and employee ID.
3. Enter basic pay, allowances, overtime hours, overtime rate, and incentives.
4. Validate that all salary inputs are non-negative.
5. Calculate overtime pay by multiplying overtime hours by the overtime rate.
6. Calculate gross salary using the formula:
   Gross Salary = Basic Pay + Allowances + Overtime Pay + Incentives
7. Calculate progressive deductions using the following example slabs:
   - First ₹10,000: No deduction.
   - Next ₹10,000: 5% deduction.
   - Amount above ₹20,000: 10% deduction.
8. Calculate net salary using the formula:
   Net Salary = Gross Salary − Total Deductions
9. Display the employee details, earnings, deductions, and net salary in a formatted salary statement.
10. Stop the program.
Note: The deduction slabs used here are illustrative rules for this project, not official tax or payroll rules.
# Mermaid flowchart
```flowchart TD
    A([Start]) --> B[/Enter employee details and salary inputs/]
    B --> C{Are inputs valid?}
    C -- No --> D[Display Invalid Input]
    D --> Z([Stop])
    C -- Yes --> E[Calculate Overtime Pay]
    E --> F[Calculate Gross Salary]
    F --> G{Gross Salary <= 10000?}
    G -- Yes --> H[Deduction = 0]
    G -- No --> I{Gross Salary <= 20000?}
    I -- Yes --> J[Deduction = 5% of amount above 10000]
    I -- No --> K[Deduction = 500 + 10% of amount above 20000]
    H --> L[Calculate Net Salary]
    J --> L
```
# Input Code
This program accepts the employee's details and salary components.
# Employee Payroll Input Program

name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")

basic = float(input("Enter basic pay: "))
allowances = float(input("Enter allowances: "))
hours = float(input("Enter overtime hours: "))
rate = float(input("Enter overtime rate per hour: "))
incentives = float(input("Enter incentives: "))

print("Employee Name:", name)
print("Employee ID:", emp_id)
print("Basic Pay:", basic)
print("Allowances:", allowances)
print("Overtime Hours:", hours)
print("Overtime Rate:", rate)
print("Incentives:", incentives)
# sample input
Enter employee name: Ravi
Enter employee ID: E101
Enter basic pay: 18000
Enter allowances: 3000
Enter overtime hours: 10
Enter overtime rate per hour: 100
Enter incentives: 2000
# expected output
========== SALARY STATEMENT ==========
Employee Name : Ravi
Employee ID   : E101
--------------------------------------
Basic Pay     : Rs. 18000.0
Allowances    : Rs. 3000.0
Overtime Pay  : Rs. 1000.0
Incentives    : Rs. 2000.0
--------------------------------------
Gross Salary  : Rs. 24000.0
Deductions    : Rs. 900.0
Net Salary    : Rs. 23100.0
======================================

    K --> L
    L --> M[Generate Salary Statement]
    M --> N([Stop])
