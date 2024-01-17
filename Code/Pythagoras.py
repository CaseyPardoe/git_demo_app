
print("Please choose which calculation you wish to make")
print("1. Find the length of A given B and C")
print("2. Find the length of B given A and C")
print("3. Find the length of C given A and B")

calc = int(input())

if calc == 1:
    num_1 = int(input(print("Please enter the length of side B ")))
    num_2 = int(input(print("Please enter the length of side C ")))

    print(f"The length of side A is {num_2 - num_1}")

elif calc == 2:
    num_1 = int(input(print("Please enter the length of side A ")))
    num_2 = int(input(print("Please enter the length of side C ")))

    print(f"The length of side A is {num_2 - num_1}")

elif calc == 3:
    num_1 = int(input(print("Please enter the length of side A ")))
    num_2 = int(input(print("Please enter the length of side B ")))

    print(f"The length of side A is {num_2 ** 2 + num_1 ** 2}")

else:
    print("Please select a valid calculation number")