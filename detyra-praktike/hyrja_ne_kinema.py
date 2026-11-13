age = int(input("Shkruaj moshen: "))
ticket = input("A ke bilete? ")

if age >= 16 and ticket == "po":
    print("Hyrja u lejua")
elif age < 16 or ticket != "po":
    print("Hyrja u refuzua")
