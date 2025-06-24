# def sum_porblem(arr):
#     result = []
#     n = len(arr)
#     for i in range(n-2):
#         for j in range(i+1,n-1):
#             for k in range(j+1,n):
#                 if arr[i]+arr[j]+arr[k] == 0 :
#                     result.append([arr[i],arr[j],arr[k]])
#     return result

# arr = [-1,0,1,2,-1,-4]
# abc = sum_porblem(arr)
# print(abc)

# def sum_of_3(arr):
#     n = len(arr)
#     arr.sort()
#     result = []
#     new_arrr = []
#     for i in range(n-2):
#         new_arrr.append([arr[i],arr[i+1],arr[i+2]])
#     n = len(new_arrr)
#     for i in range(n):
#         if new_arrr[i][0] + new_arrr[i][1] + new_arrr[i][2] == 0:
#             result.append(new_arrr[i])
#     return result

# arr = [-1,0,1,2,-1,-4]
# abc = sum_of_3(arr)
# print(abc)


def threeSum(nums):
        n = len(nums)
        result = set()
        for i in range(n):
            hashset = set()
            for j in range(i + 1, n):
                third = -(nums[i] + nums[j])
                if third in hashset:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    result.add(tuple(temp))
                hashset.add(nums[j])

        ans = list(result)
        return ans

arr = [-1, 0, 1, 2, -1, -4]
abc = threeSum(arr)
print(abc)
