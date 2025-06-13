def max_profit(Arr):
    n = len(Arr)
    max_profit = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if Arr[j] > Arr[i]:
                profit = Arr[j] - Arr[i]
                max_profit = max(max_profit, profit)
    return max_profit

abc = [7, 1, 5, 3, 6, 4]
result = max_profit(abc)
print(result)  # Output: 5 (Buy at 1 and sell at 6)
