num = int(input("Please input a number "))
factorial = 1

while num > 1:
    factorial *= num 
    num -= 1
print("factorial is ", factorial)