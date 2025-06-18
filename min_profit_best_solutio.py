def min_profit_best_solution(Arr):
    n = len(Arr)
    min_price = Arr[0]
    max_profit = 0
    for i in range(0,n):
        min_price = min(min_price, Arr[i])
        max_profit = max(max_profit, Arr[i] - min_price)
    return max_profit
abc = [7, 1, 5, 3, 6, 4]
result = min_profit_best_solution(abc)
print(result)  # Output: 5 (Buy at 1 and sell at 6)

