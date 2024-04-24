def getIncomeTax(pa=11850):
    return salary - pa

salary = int(input("Please enter your salary: "))
salary = getIncomeTax()

if salary <= 34500:
    print((salary * 20) / 100)
elif salary <= 150000:
    print((salary * 45) / 100)
elif salary > 150000:
    print((salary * 45) / 100)
