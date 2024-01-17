while True:
    maths_mark = int(input("Enter maths mark (0-100): "))
    if 0 <= maths_mark <= 100:
        break
    else:
        print("Invalid input. Please enter a valid maths mark (0-100).")

while True:
    english_mark = int(input("Enter english mark (0-100): "))
    if 0 <= english_mark <= 100:
        break
    else:
        print("Invalid input. Please enter a valid english mark (0-100).")

while True:
    ict_mark = int(input("Enter ict mark (0-100): "))
    if 0 <= ict_mark <= 100:
        break
    else:
        print("Invalid input. Please enter a valid ict mark (0-100).")

average_mark = (maths_mark + english_mark + ict_mark) / 3

if average_mark >= 65:
    result = "pass"
else:
    result = "fail"

print(f"Average mark: {average_mark}: {result}")