orders = [
    {"id": 101, "city": "Vushtrri", "amount": 25.50, "status": "Delivered"},
    {"id": 102, "city": "Prishtinë", "amount": 40.00, "status": "Delivered"},
    {"id": 103, "city": "Mitrovicë", "amount": -10.00, "status": "Delivered"},
    {"id": 104, "city": "Vushtrri", "amount": 18.00, "status": "Cancelled"},
    {"id": 105, "city": "Prishtinë", "amount": 62.50, "status": "Delivered"},
    {"id": 102, "city": "Prishtinë", "amount": 40.00, "status": "Delivered"},
    {"id": 106, "city": "Mitrovicë", "amount": 33.00, "status": "Delivered"},
    {"id": 107, "city": "Vushtrri", "amount": 47.00, "status": "Delivered"},
]

seen_ids = []
clean_orders = []
duplicate_count = 0
invalid_count = 0
cancelled_count = 0

print("===== CLEANING =====")
for order in orders:
    order_id = order["id"]

    if order_id in seen_ids:
        duplicate_count += 1
        print(f"Order {order_id}: DUPLICATE - skipped")
    else:
        seen_ids.append(order_id)

        if order["amount"] <= 0:
            invalid_count += 1
            print(f"Order {order_id}: INVALID AMOUNT - skipped")
        elif order["status"] == "Cancelled":
            cancelled_count += 1
            print(f"Order {order_id}: CANCELLED - skipped")
        else:
            clean_orders.append(order)
            print(f"Order {order_id}: OK")

revenue_by_city = {}
orders_by_city = {}

for order in clean_orders:
    city = order["city"]

    if city in revenue_by_city:
        revenue_by_city[city] += order["amount"]
        orders_by_city[city] += 1
    else:
        revenue_by_city[city] = order["amount"]
        orders_by_city[city] = 1

total_revenue = 0
best_city = ""
best_revenue = 0

print("===== REPORT BY CITY =====")
for city, revenue in revenue_by_city.items():
    count = orders_by_city[city]
    average = revenue / count
    print(f"{city}: {count} orders | {revenue:.2f} EUR | avg {average:.2f} EUR")

    total_revenue += revenue
    if revenue > best_revenue:
        best_city = city
        best_revenue = revenue

print("--------------------------")
print(f"Raw Orders: {len(orders)}")
print(f"Clean Orders: {len(clean_orders)}")
print(
    f"Skipped: {duplicate_count} duplicate, {invalid_count} invalid, {cancelled_count} cancelled"
)
print(f"Total Revenue: {total_revenue:.2f} EUR")
print(f"Best City: {best_city} ({best_revenue:.2f} EUR)")
print("==========================")
