num_1 = int(input("Please input your first number: "))
num_2 = int(input("Please input your second number: "))

print("Add +")
print("Subtract -")
print("Multiply *")
print("Divide /")
print("Square s")

calc = str(input(" Please enter which calculation to use ")).lower()

if calc in "+":
   print(f"Here is your result {num_1 + num_2}")

elif calc in "-":
   print(f"Here is your result {num_1 - num_2}")

elif calc in "*":
   print(f"Here is your result {num_1 * num_2}")

elif calc in "/":
   print(f"Here is your result {num_1 / num_2}")

elif calc in "s":
   print(f"Here is your result {num_1 ** num_2}")

else:
   print("Please enter actual number and presented calculation name")