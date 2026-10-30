# Campus Event Financial Planning

import math

venue = float(input("Enter venue cost: Rs. "))
equipment = float(input("Enter equipment cost: Rs. "))
transport = float(input("Enter transport cost: Rs. "))

catering = float(input("Enter catering cost per participant: Rs. "))
certificate = float(input("Enter certificate cost per participant: Rs. "))

participants = int(input("Enter expected participants: "))
registration = float(input("Enter registration fee per participant: Rs. "))
sponsorship = float(input("Enter sponsorship amount: Rs. "))

# Validate inputs
if (venue < 0 or equipment < 0 or transport < 0 or
    catering < 0 or certificate < 0 or participants <= 0 or
    registration < 0 or sponsorship < 0):

    print("Invalid input! Enter valid non-negative values.")

else:
    # Calculate costs
    fixed_cost = venue + equipment + transport
    variable_cost = (catering + certificate) * participants
    total_cost = fixed_cost + variable_cost

    # Calculate contributions
    participant_contributions = registration * participants
    total_funds = participant_contributions + sponsorship

    shortfall = max(0, total_cost - total_funds)

    # Calculate break-even registrations
    cost_per_participant = catering + certificate
    contribution_per_participant = registration - cost_per_participant
    remaining_fixed_cost = max(0, fixed_cost - sponsorship)

    print("\n--- Campus Event Financial Report ---")
    print("Fixed Costs: Rs.", round(fixed_cost, 2))
    print("Catering and Certificate Costs: Rs.",
          round(variable_cost, 2))
    print("Total Event Cost: Rs.", round(total_cost, 2))
    print("Participant Contributions: Rs.",
          round(participant_contributions, 2))
    print("Sponsorship: Rs.", round(sponsorship, 2))
    print("Sponsorship/Funding Shortfall: Rs.",
          round(shortfall, 2))

    if shortfall == 0:
        print("Status: Event expenses are fully covered.")
    else:
        print("Status: Additional funding is required.")

    if remaining_fixed_cost == 0:
        break_even = 0
        print("Break-Even Registrations: 0")
        print("Sponsorship covers all fixed costs.")
    elif contribution_per_participant > 0:
        break_even = math.ceil(
            remaining_fixed_cost / contribution_per_participant
        )
        print("Minimum Break-Even Registrations:", break_even)
    else:
        print("Break-even cannot be achieved through registrations alone.")
