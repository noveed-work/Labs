def getIncomeTax(pa=11850):
    return salary - pa

<<<<<<< HEAD
salary = int(input("Please enter your salary: £"))
=======
salary = int(input("Please enter your salary: £ "))
>>>>>>> b6fe08b030f126d4fa7931fbd31d8e92ed836116
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
