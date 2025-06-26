def max_count_func(arr,key):
    count = 0
    max_count = 0
    for i in range(len(arr)):
        if arr[i] == key:
            count += 1
        else:
            max_count = max(count,max_count)
            count = 0
    return max(count,max_count)



# Example usage
arr = [1, 2,5,5,5,5,54, 5, 6, 7, 8, 9,5,5,5, 10]
key = 5 
print(max_count_func(arr, key))  # Output: 5
