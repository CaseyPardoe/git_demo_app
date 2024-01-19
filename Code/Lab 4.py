# List of ages
ages = [12, 18, 33, 84, 45, 67, 12, 82, 95, 16, 10, 23, 43, 29, 40, 34, 30, 16, 44, 69, 70, 74, 38, 65, 36, 83, 50, 11, 79, 64, 78, 37, 3, 8, 68, 22, 4, 60, 33, 82, 45, 23, 5, 18, 28, 99, 17, 81, 14, 88, 50, 19, 59, 7, 44, 93, 35, 72, 25, 63, 11, 69, 11, 76, 10, 60, 30, 14, 21, 82, 47, 6, 21, 88, 46, 78, 92, 48, 36, 28, 51]

# Exercise 1
length_of_ages = len(ages)
print(f"Length of ages list: {length_of_ages}")

# Exercise 2
print("Ages:")
for age in ages:
    print(age)

# Exercise 3
for i in range(length_of_ages):
    ages[i] += 1
print("Ages after adding one year:")
print(ages)

# Exercise 4
for age in ages[:]:  # Creating a copy of ages to avoid issues with deletion
    if age < 16 or age > 65:
        ages.remove(age)
print("Ages within the range 16-65:")
print(ages)

# Exercise 5
count_16_25 = sum(1 for age in ages if 16 <= age <= 25)
print(f"Count of 16-25 year olds: {count_16_25}")

# Exercise 6
ages.sort()
print("Sorted ages:")
print(ages)

# Exercise 7
count_16_25_proportion = count_16_25 / length_of_ages
print(f"Proportion of ages between 16-25: {count_16_25_proportion:.2%}")
