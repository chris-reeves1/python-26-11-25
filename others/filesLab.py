import csv

companies = []
sales = []

with open("output.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        companies.append(row[0])
        sales.append([int(x.replace(",", "")) for x in row[1: ]])

print(sales)

monthly_sum = [sum(x) for x in zip(*sales)]
print(monthly_sum)

yearly_sum = {}
for i in range(len(companies)):
    yearly_sum[companies[i]] = sum(sales[i])


print("yearly sales: ")
for compnay, sales in yearly_sum.items():
    print(compnay, sales)