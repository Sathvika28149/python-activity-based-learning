# Railway Fare and Reservation Calculator

total_booking = 0
total_penalty = 0

n = int(input("Enter number of passengers: "))

for i in range(n):
    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter distance in km: "))

    print("Classes: Sleeper, AC3, AC2")
    travel_class = input("Enter travel class: ").upper()

    cancel = input("Cancel ticket? (yes/no): ").lower()

    # Validate inputs
    if age < 0 or distance <= 0:
        print("Invalid age or distance.")
        continue

    if travel_class not in ["SLEEPER", "AC3", "AC2"]:
        print("Invalid travel class.")
        continue

    # Calculate distance-based fare
    if distance <= 100:
        fare = distance * 1.50
    elif distance <= 500:
        fare = 100 * 1.50 + (distance - 100) * 1.20
    else:
        fare = 100 * 1.50 + 400 * 1.20 + (distance - 500) * 1.00

    # Apply class multiplier
    if travel_class == "SLEEPER":
        multiplier = 1.0
    elif travel_class == "AC3":
        multiplier = 1.5
    else:
        multiplier = 2.0

    fare = fare * multiplier

    # Apply age concession
    if age < 5:
        concession = fare
    elif age >= 60:
        concession = fare * 0.20
    else:
        concession = 0

    fare_after_concession = fare - concession
    reservation_fee = 40
    final_fare = fare_after_concession + reservation_fee

    # Cancellation calculation
    print("\n--- Fare Details ---")
    print("Passenger:", name)
    print("Basic Fare:", round(fare, 2))
    print("Age Concession:", round(concession, 2))
    print("Reservation Fee:", reservation_fee)
    print("Ticket Fare:", round(final_fare, 2))

    if cancel == "yes":
        penalty = fare_after_concession * 0.25
        total_penalty += penalty

        print("Cancellation Penalty:", round(penalty, 2))
        print("Refund Amount:", round(final_fare - penalty, 2))
    else:
        total_booking += final_fare
        print("Amount Payable:", round(final_fare, 2))

print("\n--- Booking Summary ---")
print("Total Booking Amount: Rs.", round(total_booking, 2))
print("Total Cancellation Penalty: Rs.", round(total_penalty, 2))
