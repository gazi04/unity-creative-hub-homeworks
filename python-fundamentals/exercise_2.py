VAT_PERCENT = 18

customer_name = input("Customer name: ")
product = input("Product name: ")
unit_price = float(input("Product price (EUR): "))
quantity = int(input("Quantity: "))
discount_percent = float(input("Discount percentage (%): "))
shipping = float(input("Shipping cost (EUR): "))

subtotal = unit_price * quantity
discount_amount = subtotal * discount_percent / 100
price_after_discount = subtotal - discount_amount
amount_before_vat = price_after_discount + shipping
vat_amount = amount_before_vat * VAT_PERCENT / 100
total = amount_before_vat + vat_amount

print()
print("======= ORDER INVOICE =======")
print(f"Customer: {customer_name}")
print(f"Product: {product}")
print(f"Unit Price: {unit_price:.2f} EUR")
print(f"Quantity: {quantity}")
print()
print(f"Subtotal: {subtotal:.2f} EUR")
print(f"Discount ({discount_percent:g}%): {discount_amount:.2f} EUR")
print(f"Shipping: {shipping:.2f} EUR")
print(f"VAT ({VAT_PERCENT}%): {vat_amount:.2f} EUR")
print()
print(f"TOTAL: {total:.2f} EUR")
print("=============================")
