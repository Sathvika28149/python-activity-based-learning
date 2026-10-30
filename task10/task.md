# Problem Statement
Develop a Python program to calculate the total cost of organizing a campus event, including venue, equipment, catering, transport, and certificates. The program calculates participant contributions, checks whether sponsorship covers the remaining cost, and determines the minimum number of registrations required to break even.
# Algorithm
1. Start the program.
2. Enter the venue cost, equipment cost, catering cost, transport cost, and certificate cost per participant.
3. Enter the expected number of participants.
4. Enter the registration fee per participant.
5. Enter the sponsorship amount.
6. Calculate total fixed costs:
   - Fixed cost = Venue cost + Equipment cost + Transport cost.
7. Calculate participant costs:
   - Participant cost = (Catering cost per participant + Certificate cost per participant) × Number of participants.
8. Calculate total event cost by adding fixed costs and participant costs.
9. Calculate total registration contributions:
   - Registration contributions = Registration fee × Number of participants.
10. Calculate the sponsorship shortfall, if any.
11. Calculate the minimum registrations needed to cover the event cost after sponsorship.
12. Display the total cost, participant contributions, sponsorship shortfall, and break-even registration count.
13. Stop the program.
# Mermaid Flowchart
```flowchart TD
    A([Start]) --> B[/Enter event costs and participant details/]
    B --> C{Are inputs valid?}
    C -- No --> D[Display Invalid Input]
    D --> Z([Stop])
    C -- Yes --> E[Calculate Fixed Costs]
    E --> F[Calculate Catering and Certificate Costs]
    F --> G[Calculate Total Event Cost]
    G --> H[Calculate Registration Contributions]
    H --> I[Calculate Sponsorship Shortfall]
```
Input Code
This program accepts the event details and displays the entered values.
# Campus Event Financial Planning

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
transport = float(input("Enter transport cost: "))
catering = float(input("Enter catering cost per participant: "))
certificate = float(input("Enter certificate cost per participant: "))

participants = int(input("Enter expected participants: "))
registration = float(input("Enter registration fee per participant: "))
sponsorship = float(input("Enter sponsorship amount: "))

print("\n--- Event Details ---")
print("Venue Cost:", venue)
print("Equipment Cost:", equipment)
print("Transport Cost:", transport)
print("Catering Cost per Participant:", catering)
print("Certificate Cost per Participant:", certificate)
print("Expected Participants:", participants)
print("Registration Fee:", registration)
print("Sponsorship:", sponsorship)
# sample input
### Sample Input

```text
Enter venue cost: Rs. 10000
Enter equipment cost: Rs. 5000
Enter transport cost: Rs. 3000
Enter catering cost per participant: Rs. 200
Enter certificate cost per participant: Rs. 50
Enter expected participants: 100
Enter registration fee per participant: Rs. 300
Enter sponsorship amount: Rs. 15000
```

### Sample Output

```text
--- Campus Event Financial Report ---
Fixed Costs: Rs. 18000.0
Catering and Certificate Costs: Rs. 25000.0
Total Event Cost: Rs. 43000.0
Participant Contributions: Rs. 30000.0
Sponsorship: Rs. 15000.0
Sponsorship/Funding Shortfall: Rs. 0
Status: Event expenses are fully covered.
Minimum Break-Even Registrations: 36
```

### Calculation

- Fixed costs = ₹10,000 + ₹5,000 + ₹3,000 = ₹18,000
- Variable cost per participant = ₹200 + ₹50 = ₹250
- Total event cost = ₹18,000 + ₹25,000 = ₹43,000
- Participant contributions = 100 × ₹300 = ₹30,000
- Total funds = ₹30,000 + ₹15,000 = ₹45,000
- Surplus = ₹45,000 − ₹43,000 = ₹2,000
- Break-even registrations = ₹18,000 ÷ (₹300 − ₹250) = **360 registrations** if sponsorship is not allocated to fixed costs; with ₹15,000 sponsorship allocated to fixed costs, it is **60 registrations**.
    I --> J[Calculate Break-Even Registrations]
    J --> K[Display Financial Report]
    K --> Z
