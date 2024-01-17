milkshakes = {
    1: {"flavor": "Chocolate", "price": 3.50},
    2: {"flavor": "Strawberry", "price": 4.00},
    3: {"flavor": "Vanilla", "price": 3.00},
    # Add more milkshake options if needed
}

budget = float(input("Sam, what's your budget for the milkshake therapy? $"))

while True:
    print("\nMilkshake Menu:")
    for number, shake in milkshakes.items():
        print(f"{number}: {shake['flavor']} - ${shake['price']}")

    choice = input("What can I fix you? (Enter the number or Q to quit): ").upper()

    if choice == 'Q':
        print("Sam, good luck in your search for love. Have a great day!")
        break

    if choice.isnumeric():
        choice = int(choice)
        if choice in milkshakes:
            price = milkshakes[choice]["price"]
            if budget >= price:
                budget -= price
                print(f"You've ordered a {milkshakes[choice]['flavor']} milkshake. Remaining budget: ${budget:.2f}")
            else:
                print("Sorry, you can't afford that. You've been thrown out!")
                break
        else:
            print("Invalid choice. Please select a valid number from the menu.")
    else:
        print("Invalid input. Please enter a valid number or 'Q' to quit.")
