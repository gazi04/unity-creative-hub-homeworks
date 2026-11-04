freelancer_name = input("Freelancer name: ")
hours = float(input("Hours worked: "))
hourly_rate = float(input("Hourly rate (EUR): "))
bonus = float(input("Monthly bonus (EUR): "))
tax_percent = float(input("Tax percentage (%): "))

base_income = hours * hourly_rate
gross_income = base_income + bonus
tax_amount = gross_income * tax_percent / 100
net_income = gross_income - tax_amount

print()
print("====== FREELANCER REPORT ======")
print(f"Freelancer: {freelancer_name}")
print(f"Hours Worked: {hours:g}")
print(f"Hourly Rate: {hourly_rate:.2f} EUR")
print()
print(f"Base Income: {base_income:.2f} EUR")
print(f"Bonus: {bonus:.2f} EUR")
print(f"Gross Income: {gross_income:.2f} EUR")
print(f"Tax ({tax_percent:g}%): {tax_amount:.2f} EUR")
print()
print(f"NET INCOME: {net_income:.2f} EUR")
print("===============================")
