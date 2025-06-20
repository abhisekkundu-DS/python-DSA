def two_sum(arr,sum):
    n = len(arr)
    abc1 ,abc2 = -1,-1
    for i in range(n):
        first = arr[i]
        for j in range(i+1,n):
            second = arr[j]
            if first + second == sum:
                abc1 = i
                abc2 = j
    return abc1,abc2
                

abc = [5,9,1,2,4,15,6,3]
sum = 13
print(two_sum(abc, sum))  # Output: (1, 5) or (5, 1) depending on the order of elements
