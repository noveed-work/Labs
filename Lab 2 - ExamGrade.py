grade = int(input("Please enter your grade: "))

while grade<0 or grade>101:
    print("Error: marks must be between 1 and 100")
    grade = int(input("Please enter your grade: "))
if grade<50:
    print("Fail")
elif grade<60:
    print("Pass")
elif grade<71:
    print("Merit")
elif grade<100:
    print("Distinction")