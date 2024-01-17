shakes = {1: "Chocolate Dream ($5)", 2: "Strawberry Swirl ($4)", 3: "Vanilla Bean Bliss ($3)"}
wallet = 10

while True:
    choice = input("Shake number (q to quit): ").lower()
    if choice == "q": break

    choice = int(choice)  # Convert input to integer

    if choice in shakes:
        shake, price = shakes[choice].split("$")
        price = int(price)
        if price <= wallet:
            wallet -= price
            print(f"Sam sips {shake}. Not as sweet as his ex.")
        else:
            print("Can't afford that one.")
    else:
        print("Unknown shake.")

    print(f"Remaining wallet: ${wallet}")  # Display remaining budget

print("Come back soon, Sam!")
