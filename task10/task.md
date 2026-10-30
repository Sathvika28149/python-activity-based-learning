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
    I --> J[Calculate Break-Even Registrations]
    J --> K[Display Financial Report]
    K --> Z
```
# Input Code
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
