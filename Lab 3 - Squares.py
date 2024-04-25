number = 1

while number <= 100:
    square = number ** 2
    print(f"{number} squared is {square}")
    if square > 2000:
        break
    number += 1