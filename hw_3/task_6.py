day_revenue = []
day_count = 0
while day_count < 7:
    user_input = float(input("Write your revenue per day: "))
    day_revenue.append(user_input)
    day_count += 1
week_sales = sum(day_revenue)

print(week_sales)