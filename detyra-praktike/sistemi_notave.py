for student in range(1, 6):
    points = int(input(f"Studenti {student} - Piket: "))

    if points >= 90 and points <= 100:
        print("Shkelqyeshem")
    elif points >= 70 and points <= 89:
        print("Mire")
    elif points >= 50 and points <= 69:
        print("Kalueshem")
    elif points >= 0 and points <= 49:
        print("Nuk kaloi")
    else:
        print("Pike te pavlefshme")

    print()
