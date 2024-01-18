while True:
    print("Time Calculator")
    print("1- Add 2 date-times")
    print("2- Find the difference between 2 date-times")
    print("3- Convert datetime to Hours")
    print("4- Convert datetime to Minutes")
    print("5- Convert Minutes to date-time")
    print("6- Convert Hours to date-time")
    print("7- Exit")

    choice = input("Enter an option: ")

    if choice == 1:
        while True:
            date_time1 = input("Please enter first time in DD:HH:MM: ")
            time1 = date_time1.split(':')
