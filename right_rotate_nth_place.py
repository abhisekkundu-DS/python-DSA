def right_rotate_nth_place(arr,k):
    n = len(arr)
    rotate = k % n
    for _ in range(rotate):
        # temp = arr[n-1]
        # for i in range(n-2, -1, -1):
        #     arr[i+1] = arr[i]
        # arr[0] = temp
        e = arr.pop()
        arr.insert(0,e) #inplace sorting algoritham
    
    return arr

arr = [1, 2, 3, 4, 5]
print("Before rotation:", arr)
arr = right_rotate_nth_place(arr, 2)
print("After rotation:", arr)
