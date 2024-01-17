mark = int(input("Please enter your Exam Mark: "))

if mark in range(71, 101):
    print("Distinction")

elif mark in range(61, 71):
    print("Merit")

elif mark in range(50, 61):
    print("Pass")

elif mark in range(1, 50):
    print("Fail")

else:
    print("Error: marks must be between 1 and 100")