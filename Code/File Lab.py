import csv

companies = []
sales = []

with open('output.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        companies.append(row[0])
        sales.append([int(value.replace(',', '')) for value in row[1:]])

monthly_sum = [sum(x) for x in zip(*sales)]

yearly_sum = {}
for company, monthly_sales in zip(companies, sales):
    yearly_sum[company] = sum(monthly_sales)

print("Sales data for each month:")
for month, total_sales in zip(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"], monthly_sum):
    print(f"{month}: {total_sales}")

print("\nTotal yearly sales by each manufacturer:")
for company, total in yearly_sum.items():
    print(f"{company}: {total}")
