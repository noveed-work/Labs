#   Task 4 – Input an Integer Between Two Limits
#   In this part you'll ask the user to input an integer between a minimum and maximum values.
# 	If the user fails to enter an acceptable value for three times then you stop asking!
#   1.	Add a new file: getInt.py and make it the startup file.
#   2.	Create two variables for the min and max values. 
#   Set two values for these variables such as 1 and 100.
#   3.	Write a while loop that attempts to get an integer from the user between the limits of min and max values.
#   4.	If the user has tried three times and fails then print None. 
#   If a valid value is entered, just end the loop and print its value.

#   Note: None is a valid keyword in Python which stands for Null.


number = int(input("Enter number: "))
incorrect_input = 0

while incorrect_input < 3:
    if number < 1 or number > 100:
        print("Incorrect input - please enter a number between 1 and 100")
        number = int(input("Enter number: "))
        incorrect_input += 1
    else:  
        print(f"Your number is {number}")
        break  

if incorrect_input == 3:  
    print("You have exceeded 3 attempts")