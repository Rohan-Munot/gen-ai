# used for saving memory
daily_sales = [5, 10 , 12 ,9, 43,43,22,1]
total_cups = sum( sale for sale in daily_sales if sale > 10)
print(f"total_cups: {total_cups}")