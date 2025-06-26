def abcd(arr):
    n = len(arr)
    maxi  = 0 
    for i in range(n):
        total = 0
        for j in range(i,n):
            total = total + arr[j]
            maxi = max(maxi, total)
    return maxi


    abc = [1, 2, -3, 4, 5]
    pqr = abcd(abc)
    print(pqr)  # Output: 7 (1 + 2 + 4 + 5 = 12, but the max subarray is [4, 5] which gives 9)
