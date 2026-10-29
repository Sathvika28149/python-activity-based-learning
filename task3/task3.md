# Problem Statement
To develop a Python program that calculates hospital bills by processing consultation, diagnostic, and treatment charges. The system applies concessions based on predefined conditions, validates billing constraints, and classifies patients according to their payment status and the hospital's payment policy.
# Algorithm
1. Start the program.
2. Enter the patient's name and patient type.
3. Enter consultation, diagnostic, and treatment charges.
4. Validate that all charges are non-negative.
5. Calculate the total bill by adding all charges.
6. Apply a 10% concession if the total bill is ₹10,000 or more.
7. Calculate the final bill after deducting the concession.
8. Enter the amount paid by the patient.
9. Validate that the payment is not negative or greater than the final bill.
10. Calculate the outstanding balance.
11. Classify the patient:
    - Fully Paid: No outstanding balance.
    - Partially Paid: Some amount is paid, but a balance remains.
    - Unpaid: No payment has been made.
12. Display the total bill, concession, final bill, amount paid, and patient classification.
13. Stop the program.
Note: The charges, concession percentage, and classification rules are illustrative examples for this project. Actual hospital policies may differ.
``` flowchart TD
    A([Start]) --> B[/Enter patient details and charges/]
    B --> C{Are charges valid?}
    C -- No --> D[Display Invalid Charges]
    D --> Z([Stop])
    C -- Yes --> E[Calculate Total Bill]
    E --> F{Total Bill >= 10000?}
    F -- Yes --> G[Apply 10 percent concession]
    F -- No --> H[No concession]
    G --> I[Calculate Final Bill]
    H --> I
    I --> J[/Enter Amount Paid/]
    J --> K{Is payment valid?}
    K -- No --> L[Display Invalid Payment]
    L --> Z
    K -- Yes --> M[Calculate Outstanding Balance]
    M --> N{Amount Paid = Final Bill?}
    N -- Yes --> O[Classify as Fully Paid]
    N -- No --> P{Amount Paid > 0?}
    P -- Yes --> Q[Classify as Partially Paid]
    P -- No --> R[Classify as Unpaid]
    O --> S[Display Bill and Classification]
    Q --> S
    R --> S
    S --> Z
```
# Input Code
This program accepts the patient's details, hospital charges, and payment amount.. Input Code
# Hospital Billing Input Program

name = input("Enter patient name: ")
patient_type = input("Enter patient type: ")

consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

paid = float(input("Enter amount paid: "))

print("Patient Name:", name)
print("Patient Type:", patient_type)
print("Consultation Charges:", consultation)
print("Diagnostic Charges:", diagnostic)
print("Treatment Charges:", treatment)
print("Amount Paid:", paid)
# sample input
Enter patient name: Ravi
Enter patient type: General
Enter consultation charges: 1000
Enter diagnostic charges: 3000
Enter treatment charges: 8000
Enter amount paid: 10000
# expected output
--- Hospital Bill ---
Patient Name: Ravi
Patient Type: General
Total Bill: Rs. 12000.0
Concession: Rs. 1200.0
Final Bill: Rs. 10800.0

Enter amount paid: 10000

--- Payment Details ---
Amount Paid: Rs. 10000.0
Outstanding Balance: Rs. 800.0
Patient Classification: Partially Paid
