# Task1 - Squares
#       1.	Add a new file: Squares.py to your existing Solution and make it the startup file. 
#       2.	Write a while loop that starts at 1 and ends at 100.  
#       3.	Calculates and display each number and its square.  
#       4.	End the loop if that square is bigger than 2000.  
#       5.	Save and run.  


number = 1

while number <= 100:
    square = number ** 2
    print(f"{number} squared is {square}")
    if square > 2000:
        break
    number += 1