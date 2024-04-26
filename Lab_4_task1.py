ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

num_ages = len(ages)
print("Length of ages list:", num_ages)

print("Ages:")
for age in ages:
    print(age)

for i in range(len(ages)):
    ages[i] += 1

print("Ages after adding one year to each:\n")
print(ages)

i = 0
while i < len(ages):
    if ages[i] < 16 or ages[i] > 65:
        del ages[i]
    else:
        i += 1

print("\nAges after removing ages outside the range of 16-65:\n")
print(ages)

count_16_to_25 = sum(1 for age in ages if 16 <= age <= 25)
print("Count of 16-25 year olds:", count_16_to_25)

ages.sort()
print("\nSorted ages list:")
print(ages)

proportion_16_to_25 = count_16_to_25 / num_ages
print("Proportion of ages between 16-25:", proportion_16_to_25)
