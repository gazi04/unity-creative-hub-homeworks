for canditate in range(1, 4):
    print(f"--- Kandidati {canditate} ---")
    age = int(input("Mosha: "))
    experience = int(input("Pervoja: "))
    answer = input("A njeh Python? ")

    knows_python = answer == "po"

    if age >= 18 and experience >= 2 and knows_python:
        print("Pranohet per interviste")
    elif not knows_python and experience < 3:
        print("Refuzohet")
    else:
        print("Kalon ne shqyrtim")

    print()
