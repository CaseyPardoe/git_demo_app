word = input("Enter a word: ")

vowel_count = 0

for char in word:
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += 1

print(f"The number of vowels in the word '{word}' is: {vowel_count}")

