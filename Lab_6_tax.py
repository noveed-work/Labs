def getIncomeTax(pa=11850):
    return salary - pa

salary = int(input("Please enter your salary: £ "))
salary = getIncomeTax()

if salary <= 34500:
    income_tax = ((salary * 20) / 100)
    print(f"The tax that you will pay is £{income_tax}")
elif salary <= 150000:
    income_tax = ((salary * 40) / 100)
    print(f"The tax that you will pay is £{income_tax}")
elif salary > 150000:
    income_tax = ((salary * 45) / 100)
    print(f"The tax that you will pay is £{income_tax}")
