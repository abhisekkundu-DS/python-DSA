def no_unique_element(arr):
    n = len(arr)
    a_map = {}
    for i in range(n):
        a_map[arr[i]] = 0
    j = 0
    for k in a_map:
        arr[j] = k
        j += 1
    return j

abc = [1, 2, 3, 4, 5, 5,5,5,5,6, 7, 8, 8,8,8,9, 10,10,10,]
print(no_unique_element(abc))
