level = int(input("Please enter your Level: "))
mark = int(input("Please enter your Exam Mark: "))


if level == 1 and mark in range(71, 101):
    print("Distinction")

elif level == 2 and mark in range(66, 101):
    print("Distinction")

elif level == 1 and mark in range(61, 71):
    print("Merit")

elif level == 2 and mark in range(51, 66):
    print("Merit")

elif level == 1 and mark in range(50, 61):
    print("Pass")

elif level == 2 and mark in range(40, 51):
    print("Pass")

elif level == 1 and mark in range(1, 50):
    print("Fail")

elif level == 2 and mark in range(1, 40):
    print("Fail")

else:
    print("Error: marks must be between 1 and 100")