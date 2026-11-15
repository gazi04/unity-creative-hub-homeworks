disk_capacity = 1000
months = 0

used_storage = float(input("Current used storage (GB): "))
growth_rate = float(input("Monthly growth (%): "))

alert_limit = disk_capacity * 0.9

while used_storage < alert_limit:
    used_storage += used_storage * growth_rate / 100
    months += 1
    print(f"Month {months}: {used_storage:.2f} GB")

print("========== ALERT ==========")
print(f"Disk reaches 90% after {months} months")
print(f"Used Storage: {used_storage:.2f} GB")

if months <= 6:
    print("Action: Buy a new disk NOW")
else:
    print("Action: Plan the upgrade")

print("===========================")
