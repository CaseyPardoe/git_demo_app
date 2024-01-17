min_val = 1
max_val = 100
num_tries = 0

while num_tries < 3:
    value = int(input(f"Please enter a valid number between {min_val} and {max_val} "))
    if min_val <= value <=max_val:
        print(f"Valid number detected: {value}")
        break
    else:
        print("Bad number, please try again")
    num_tries += 1
if num_tries == 3:
    print("None")