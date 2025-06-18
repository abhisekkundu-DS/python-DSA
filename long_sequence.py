def long_sequence(Arr):
    n = len(Arr)
    count  = 0
    least_smaller = float('-inf')
    longest = 0
    nums = sort(Arr)
    for i in range(0,n):
        num = nums[i]
        if num - 1 == least_smaller:
            count += 1
            least_smaller = num
        elif num - 1 > least_smaller:
            count = 1
            least_smaller = num 
        longest = max(longest, count)
    return longest

def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr  

abc = [1, 2, 3, 10, 11, 4, 5, 99, 100, 101, 102, 103, 104, 105]
result = long_sequence(abc) 
print(result)  # Output: 6 (The longest sequence is 1, 2, 3, 4, 5, 6)

