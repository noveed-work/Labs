print("Welcome to the income tax calculator: ")
salary = int(input("Enter Salary: "))

salary = salary - 11850

if salary <= 34500:
    income_tax = ((salary / 100) * 20)
    print(f"Your income tax is {income_tax}")
elif salary <= 150000:
    income_tax = ((salary / 100) * 40)
    print(f"Your income tax is {income_tax}")
elif salary> 150000:
    income_tax = ((salary / 100) * 45)
    print(f"Your income tax is {income_tax}")