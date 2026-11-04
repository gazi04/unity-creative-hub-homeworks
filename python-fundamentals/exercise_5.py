VAT_PERCENT = 18

store = input("Store name: ")

product1 = input("Product 1 name: ")
price1 = float(input("Product 1 price (EUR): "))
quantity1 = int(input("Product 1 quantity: "))
print()

product2 = input("Product 2 name: ")
price2 = float(input("Product 2 price (EUR): "))
quantity2 = int(input("Product 2 quantity: "))
print()

product3 = input("Product 3 name: ")
price3 = float(input("Product 3 price (EUR): "))
quantity3 = int(input("Product 3 quantity: "))
print()

discount_percent = float(input("Discount percentage (%): "))

revenue1 = price1 * quantity1
revenue2 = price2 * quantity2
revenue3 = price3 * quantity3

gross_revenue = revenue1 + revenue2 + revenue3
total_items = quantity1 + quantity2 + quantity3
discount_amount = gross_revenue * discount_percent / 100
revenue_after_discount = gross_revenue - discount_amount
vat_amount = revenue_after_discount * VAT_PERCENT / 100
final_revenue = revenue_after_discount + vat_amount
avg_revenue_per_item = final_revenue / total_items

print()
print("========== DAILY SALES REPORT ==========")
print(f"Store: {store}")
print()
print(f"Product 1: {product1}")
print(f"Price: {price1:.2f} EUR")
print(f"Quantity: {quantity1}")
print(f"Revenue: {revenue1:.2f} EUR")
print()
print(f"Product 2: {product2}")
print(f"Price: {price2:.2f} EUR")
print(f"Quantity: {quantity2}")
print(f"Revenue: {revenue2:.2f} EUR")
print()
print(f"Product 3: {product3}")
print(f"Price: {price3:.2f} EUR")
print(f"Quantity: {quantity3}")
print(f"Revenue: {revenue3:.2f} EUR")
print()
print("----------------------------------------")
print(f"Total Products Sold: {total_items}")
print(f"Gross Revenue: {gross_revenue:.2f} EUR")
print(f"Discount ({discount_percent:g}%): {discount_amount:.2f} EUR")
print(f"Revenue After Discount: {revenue_after_discount:.2f} EUR")
print(f"VAT ({VAT_PERCENT}%): {vat_amount:.2f} EUR")
print()
print(f"FINAL REVENUE: {final_revenue:.2f} EUR")
print(f"Average Revenue Per Item: {avg_revenue_per_item:.2f} EUR")
print("========================================")
