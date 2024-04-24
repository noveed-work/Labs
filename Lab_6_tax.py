def getIncomeTax(pa=11850):
    return salary - pa

salary = int(input("Please enter your salary: £ "))
salary = getIncomeTax()

if salary <= 34500:
    tax = ((salary * 20) / 100)
    print(f"The tax that you will pay is £{tax}")
elif salary <= 150000:
    tax = ((salary * 40) / 100)
    print(f"The tax that you will pay is £{tax}")
elif salary > 150000:
    tax = ((salary * 45) / 100)
    print(f"The tax that you will pay is £{tax}")
