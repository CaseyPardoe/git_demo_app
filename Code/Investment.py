investment = float(input("What is your investment? "))
interest = float(input("What is the interest rate? ")) /100
target = float(input("What is your target value? "))
years = 0

while investment < target:
    investment *= (1+ interest)
    years += 1
    print(f"it will take {years} years to grow to £{target}")
