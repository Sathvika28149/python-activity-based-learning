# Hospital Billing and Patient Classification

name = input("Enter patient name: ")
patient_type = input("Enter patient type: ")

consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

# Validate charges
if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid charges! Charges cannot be negative.")

else:
    total = consultation + diagnostic + treatment

    # Apply concession
    if total >= 10000:
        concession = total * 0.10
    else:
        concession = 0

    final_bill = total - concession

    print("\n--- Hospital Bill ---")
    print("Patient Name:", name)
    print("Patient Type:", patient_type)
    print("Total Bill: Rs.", total)
    print("Concession: Rs.", concession)
    print("Final Bill: Rs.", final_bill)

    paid = float(input("Enter amount paid: "))

    # Validate payment
    if paid < 0 or paid > final_bill:
        print("Invalid payment amount.")

    else:
        balance = final_bill - paid

        # Classify patient
        if balance == 0:
            status = "Fully Paid"
        elif paid > 0:
            status = "Partially Paid"
        else:
            status = "Unpaid"

        print("\n--- Payment Details ---")
        print("Amount Paid: Rs.", paid)
        print("Outstanding Balance: Rs.", balance)
        print("Patient Classification:", status)
