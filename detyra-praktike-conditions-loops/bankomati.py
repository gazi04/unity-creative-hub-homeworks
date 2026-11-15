balance = 280.0
correct_pin = "4321"
daily_limit = 300
fee = 0

pin = input("Enter PIN: ")

if pin == correct_pin:
    withdraw_amount = float(input("Amount to withdraw: "))
    is_your_bank_atm = input("Is this your bank's ATM? yes/no: ")

    if is_your_bank_atm == "yes":
        fee = 0
    else:
        fee = 2.5

    if 0 > withdraw_amount:
        print("Error: Invalid amount")
    elif withdraw_amount > daily_limit:
        print(f"Error: Daily limit is {daily_limit} EUR")
    elif withdraw_amount + fee > balance:
        print("Error: Insufficient funds")
    else:
        total_amount = withdraw_amount + fee
        balance -= total_amount

        print("===== RECEIPT =====")
        print(f"Withdrawn: {withdraw_amount:.2f} EUR")
        print(f"Fee: {fee:.2f} EUR")
        print(f"New Balance: {balance:.2f} EUR")
        print("===================")
else:
    print("Wrong PIN, Card blocked.")
