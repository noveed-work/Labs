print("Calculator Project")

operation = input("Which operation would you like to perform? - please select from +, -, * or / :" )

number1 = float(input("please select the first number: " ))
number2 = float(input("please select the second number: " ))

if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
