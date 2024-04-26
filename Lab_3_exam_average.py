math_mark = 0
english_mark = 0
ict_mark = 0

for subject in ["Math", "English", "ICT"]:
    while True:
        mark = input(f"Enter the mark for {subject} (enter a number between 1-100): ")
        try:
            mark = int(mark)
            if 1 <= mark <= 100:
                if subject == "Math":
                    math_mark = mark
                elif subject == "English":
                    english_mark = mark
                elif subject == "ICT":
                    ict_mark = mark
                break
            else:
                print("Invalid mark. Please enter a mark between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter an number.")

average_mark = (math_mark + english_mark + ict_mark) / 3
print(f"Your average mark is {average_mark}")


if average_mark >= 65:
    print("You have passed")
else:
    print("You have failed")


