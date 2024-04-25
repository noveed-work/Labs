number = int(input("Please enter a number: "))

factorial = 1
i = 1

while i <= number:
    factorial *= i
    i += 1

print("The factorial of", number, "is:", factorial)

# Used stackover flow to help me with this one
