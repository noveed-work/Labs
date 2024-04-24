print("Welcome to the income tax calculator: ")
salary = int(input("Enter Salary: "))

salary = salary - 11850

if salary <= 34500:
    it = ((salary / 100) * 20)
    print(f"Your income tax is {it}")
elif salary <= 150000:
    it = ((salary / 100) * 40)
    print(f"Your income tax is {it}")
elif salary> 150000:
    it = ((salary / 100) * 45)
    print(f"Your income tax is {it}")