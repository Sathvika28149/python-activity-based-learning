# Retail Billing with Multiple Discount Rules

products = []

n = int(input("Enter number of products: "))

if n <= 0:
    print("Invalid number of products.")

else:
    for i in range(n):
        print("\nProduct", i + 1)

        name = input("Enter product name: ")
        category = input("Enter category: ").lower()
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        if price < 0 or quantity <= 0:
            print("Invalid price or quantity.")
            break

        subtotal = price * quantity

        products.append({
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity,
            "subtotal": subtotal
        })

    else:
        # Calculate total subtotal
        subtotal = sum(p["subtotal"] for p in products)

        # Apply threshold discount
        if subtotal >= 5000:
            discount = subtotal * 0.10
        elif subtotal >= 3000:
            discount = subtotal * 0.05
        else:
            discount = 0

        # Maximum concession limit
        discount = min(discount, 1000)

        # Calculate tax rates
        tax_rates = {
            "electronics": 0.18,
            "clothing": 0.05,
            "grocery": 0.00
        }

        total_tax = 0

        print("\n========== ITEMIZED INVOICE ==========")
        print("Product       Qty   Subtotal   Discount   Tax")

        for p in products:
            # Allocate discount proportionally
            item_discount = (
                discount * p["subtotal"] / subtotal
                if subtotal > 0 else 0
            )

            discounted_price = p["subtotal"] - item_discount

            rate = tax_rates.get(p["category"], 0.12)
            tax = discounted_price * rate

            total_tax += tax

            print(
                p["name"],
                p["quantity"],
                round(p["subtotal"], 2),
                round(item_discount, 2),
                round(tax, 2)
            )

        # Calculate final bill
        final_bill = subtotal - discount + total_tax

        print("--------------------------------------")
        print("Total Subtotal : Rs.", round(subtotal, 2))
        print("Total Discount : Rs.", round(discount, 2))
        print("Total Tax      : Rs.", round(total_tax, 2))
        print("Final Bill     : Rs.", round(final_bill, 2))
        print("======================================")
