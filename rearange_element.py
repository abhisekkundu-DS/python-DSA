def rearange_element(Arr):
    n = len(Arr)
    result1 = []
    result2 = []
    result= []
    for i in range(0,n):
        if Arr[i] >= 0:
            result1.append(Arr[i])
        else:
            result2.append(Arr[i])
    m ,n = 0,0
    while m < len(result1) and n < len(result2):
        result.append(result1[m])
        result.append(result2[n])
        m += 1
        n += 1
    while m < len(result1):
        result.append(result1[m])
        m += 1
    while n < len(result2):
        result.append(result2[n])
        n += 1
    return result


abc = [1, -2,8,9,-7,-5 ,3, -4, 5, -6]
result = rearange_element(abc)
print(result)  # Output: [1, -2, 3, -4, 5, -6] (Rearranged with positive and negative elements)
