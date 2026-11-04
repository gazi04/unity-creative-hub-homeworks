name = input("Name: ")
income = float(input("Monthly income (EUR): "))
rent = float(input("Rent (EUR): "))
food = float(input("Food expenses (EUR): "))
transport = float(input("Transport (EUR): "))
internet = float(input("Internet (EUR): "))
other = float(input("Other expenses (EUR): "))

total_expenses = rent + food + transport + internet + other
remaining_money = income - total_expenses
spent_percent = total_expenses / income * 100
remaining_percent = remaining_money / income * 100

print()
print("======= MONTHLY BUDGET =======")
print(f"Name: {name}")
print(f"Monthly Income: {income:.2f} EUR")
print()
print(f"Rent: {rent:.2f} EUR")
print(f"Food: {food:.2f} EUR")
print(f"Transport: {transport:.2f} EUR")
print(f"Internet: {internet:.2f} EUR")
print(f"Other Expenses: {other:.2f} EUR")
print()
print(f"Total Expenses: {total_expenses:.2f} EUR")
print(f"Remaining Money: {remaining_money:.2f} EUR")
print(f"Spent: {spent_percent:.2f}%")
print(f"Remaining: {remaining_percent:.2f}%")
print("==============================")
