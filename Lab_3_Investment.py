# Task 3 - Investment 
#       1.	Add a new file: Investment.py and make it the startup file.  
#       2.	Calculates how many years it will take an initial investment of £100 to grow to a target value of £1000 if the interest rate is 10%.
#       Tip: Do not start writing code until you've a plan of action!
#       3.	Save and run.   
#  
#       4.	Make your calculation more usable by inputting the following values:
# 		Initial investment  
#       Target value  
#       Interest rate  
#       5.	Save and run.   


investment = int(input("Please enter initial investment: "))
target = int(input("Please enter your target value: "))
interest_rate = float(input("Please enter the interest rate: "))

years = 0

while investment < target:
    growth = investment * interest_rate
    investment += growth
    years += 1

print(f"It will take {years} years to reach £{target}.")

