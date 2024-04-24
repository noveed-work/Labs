import statistics

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

grades = [int(x) for x in data.split(",")]
print(grades)

minimum_value = min(grades)
print(minimum_value)

maximum_value = max(grades)
print(maximum_value)

average = sum(grades) / len(grades)
average = round(average, 2)
print(average)

mean = statistics.mean(grades)
mean = round(mean, 2)
print(mean)

median = statistics.median(grades)
median = round(median, 2)
print(median)

print(f"the min is {minimum_value}, the max is {maximum_value}, the average is {average}, the mean is {mean}, and the median is {median}")
