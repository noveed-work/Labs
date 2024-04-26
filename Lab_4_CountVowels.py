word = input("enter word: ")
vowel_count = 0

for char in word:
    if char.lower() in "aeiou":
        vowel_count += 1
print(f"Number of vowels in {word} is {vowel_count}")

