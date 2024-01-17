num = 1
while num <= 100:
    square = num ** 2
    print(num, "=", square)
    num += 1

    if num > 100 or square > 2000:
        break
  