prices = [3, 3, 5, 0, 0, 3, 1, 4]
n = len(prices)

if n < 2:
    print(0) 
    exit()

profit_one = [0] * n 
profit_two = [0] * n 

min_price = prices[0]
for i in range(1, n):
    min_price = min(min_price, prices[i])
    profit_one[i] = max(profit_one[i - 1], prices[i] - min_price)

max_price = prices[-1]
for i in range(n - 2, -1, -1):
    max_price = max(max_price, prices[i])
    profit_two[i] = max(profit_two[i + 1], max_price - prices[i])

max_profit = 0
for i in range(n):
    max_profit = max(max_profit, profit_one[i] + profit_two[i])

print(max_profit)
