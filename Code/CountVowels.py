word = input("enter a word: ")

letters = 0
vowels = 0

while letters < len(word):
    x = word[letters]
    if x in "aeiou":
        vowels +=1 
    letters += 1

print(f"number of vowels in {word} is {vowels}")