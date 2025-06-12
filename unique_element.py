def unique_element(arr):
    n = len(arr)
    abs_map  = [arr[0],]
    count = 1
    for i in range(n-1):
        if arr[i] != arr[i+1]:
            abs_map.append(arr[i+1])
            count += 1  

    return count

abc = [1, 2, 3, 4, 5, 5,5,5,5,6, 7, 8, 8,8,8,9, 10,10,10,]
print(unique_element(abc))
