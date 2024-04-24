grade = int(input("Please enter your grade: "))

while grade<1 or grade>100:
    print("Invalid grade, please enter a grade between 1 and 100")
    grade = int(input("Please enter your grade"))

level = int(input("Please enter your level: "))

while level<1 or level>2:
    print("Invalid input, please select 1 or 2")
    level = int(input("Please enter your level: "))

if level == 1:
    if grade<50:
        print("Fail")
    elif grade<60:
        print("Pass")
    elif grade<71:
        print("Merit")
    elif grade<101:
        print("Distinction")
elif level == 2:
    if grade<40:
        print("Fail")
    elif grade<50:
        print("Pass")
    elif grade<65:
        print("Merit")
    elif grade<101:
        print("Distinction")
