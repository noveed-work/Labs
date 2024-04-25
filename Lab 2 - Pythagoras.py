print("Please see below options")
print("1 = Find the length of A given B and C")
print("2 = Find the length of B given A and C")
print("3 = Find the length of C given A and B")
menu = input("Please select 1, 2 or 3: ")


if menu == "1":
    b = int(input("Please provide the lenth of B: "))
    c = int(input("Please provide the length of C: "))
    a = b**2 + b**2
    print(f"Your answer is {a}")
elif menu == "2":
    a = int(input("Please provide the lenth of A: "))
    c = int(input("Please provide the length of C: "))
    b = a**2 + c**2
    print(f"Your answer is {b}")
elif menu == "3":
    a = int(input("Please provide the lenth of A: "))
    b = int(input("Please provide the lenth of B: "))
    c = a**2 + b**2
    print(f"Your answer is {c}")