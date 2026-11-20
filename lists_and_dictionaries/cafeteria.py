menu = {
    "Espresso": 1.20,
    "Macchiato": 1.50,
    "Cappuccino": 2.00,
    "Tea": 1.00,
    "Croissant": 1.80,
}

menu["Cappuccino"] = 2.20
menu["Hot Chocolate"] = 2.50

order = {}

print("===== MENU =====")
for item, price in menu.items():
    print(f"{item}: {price:.2f} EUR")

print("================")
for i in range(1, 5):
    item = input(f"Item {i}: ")

    if item not in menu:
        print(f"Sorry, {item} not in menu.")
        continue

    quantity = int(input(f"Quantity of {item}: "))

    if item in order:
        order[item] += quantity
    else:
        order[item] = quantity


print("===== RECEIPT =====")
total = 0
for item, quantity in order.items():
    price = menu[item] * quantity
    total += price
    print(f"{item} x{quantity} = {price:.2f} EUR")
print("-------------------")

print("Different items:", len(order))
print(f"Total {total:.2f} EUR")

discount = 0
if total > 10:
    discount = total * 0.1

print(f"Discount: {discount:.2f} EUR")
print(f"To pay: {(total - discount):.2f} EUR")
print("===================")
