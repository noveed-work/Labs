investment = int(input("Please enter initial investment: "))
target = int(input("Please enter your target value: "))
interest_rate = float(input("Please enter the interest rate: "))

years = 0

while investment < target:
    growth = investment * interest_rate
    investment += growth
    years += 1

print(f"It will take {years} years for the initial investment of {investment} to grow to {target}.")

#investment gets printed incorrectly on my f string. 
