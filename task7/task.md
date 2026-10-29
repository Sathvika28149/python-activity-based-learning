# Problem Statement
To develop a Python program that processes multiple products and their quantities, calculates the total price, applies category-specific taxes, and provides discounts based on purchase thresholds. The system also enforces a maximum concession limit and generates an itemized invoice showing product details, discounts, taxes, and the final payable amount.

Note: The prices, tax rates, discount percentages, and maximum concession limit used in this project are illustrative examples.
# Algorithm
1. Start the program.
2. Enter the number of products.
3. For each product, enter its name, category, price, and quantity.
4. Calculate the subtotal for each product using price × quantity.
5. Apply the discount rules:
   - If the total purchase is ₹5,000 or more, apply a 10% discount.
   - If the total purchase is ₹3,000 or more but below ₹5,000, apply a 5% discount.
   - Otherwise, no discount is applied.
6. Limit the total discount to a maximum of ₹1,000.
7. Calculate the discounted amount.
8. Apply category-specific taxes:
   - Electronics: 18%.
   - Clothing: 5%.
   - Grocery: 0%.
   - Other categories: 12%.
9. Calculate the final bill using the formula:
   Final Bill = Subtotal − Discount + Tax
10. Generate an itemized invoice showing product names, quantities, prices, discounts, taxes, and the final amount.
11. Display the total payable amount.
12. Stop the program.
# Mermaid Flowchart
```flowchart TD
    A([Start]) --> B[/Enter number of products/]
    B --> C[/Enter product name, category, price and quantity/]
    C --> D{Are inputs valid?}
    D -- No --> E[Display Invalid Input]
    E --> Z([Stop])
    D -- Yes --> F[Calculate product subtotals]
    F --> G{More products?}
    G -- Yes --> C
    G -- No --> H[Calculate total subtotal]
    H --> I{Subtotal >= 5000?}
    I -- Yes --> J[Apply 10 percent discount]
    I -- No --> K{Subtotal >= 3000?}
    K -- Yes --> L[Apply 5 percent discount]
    K -- No --> M[No discount]
    J --> N[Limit discount to Rs. 1000]
    L --> N
    M --> O[Allocate discount to products]
    N --> O
    O --> P[Calculate category-specific taxes]
    P --> Q[Calculate final payable amount]
    Q --> R[Generate itemized invoice]
    R --> S([Stop])
```
# Input Code
This program accepts product details from the user.
# Retail Billing Input Program

n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    subtotal = price * quantity

    print("Product:", name)
    print("Category:", category)
    print("Subtotal: Rs.", subtotal)
# sample output
Enter number of products: 2

Product 1
Enter product name: Laptop
Enter category: Electronics
Enter price: 4000
Enter quantity: 1

Product 2
Enter product name: Shirt
Enter category: Clothing
Enter price: 1000
Enter quantity: 1
# sample input
Enter number of products: 2

Product 1
Enter product name: Laptop
Enter category: Electronics
Enter price: 4000
Enter quantity: 1

Product 2
Enter product name: Shirt
Enter category: Clothing
Enter price: 1000
Enter quantity: 1
# expected output
========== ITEMIZED INVOICE ==========
Product       Qty   Subtotal   Discount   Tax
Laptop        1     4000.0     400.0      648.0
Shirt         1     1000.0     100.0      45.0
--------------------------------------
Total Subtotal : Rs. 5000.0
Total Discount : Rs. 500.0
Total Tax      : Rs. 693.0
Final Bill     : Rs. 5193.0
======================================
