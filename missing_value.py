def missing_value(arr):
    n = len(arr)
    sum = (n *(n+1))//2
    arr_sum = 0
    for i in arr:
        arr_sum += i
    return sum - arr_sum

abc = [0,1, 2, 3, 4, 6, 7, 8, 9, 10]
  # Remove the missing value
print(missing_value(abc))  # Output: 5

