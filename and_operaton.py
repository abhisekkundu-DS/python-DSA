def operator(str1,str2):
    n1 = len(str1)
    n2 = len(str2)
    i ,j = 0,0
    ans = ""
    while i < n1 and j < n2:
        if (int(str1[i]) == 1 and int(str2[j]) == 1):
            ans = ans + "1"
        else:
            ans = ans + "0"
        i += 1
        j += 1
    while i < n1:
        ans = ans + str1[i]
        i += 1
    while j < n2:
        ans = ans + str2[j]
        j += 1
    return ans


# Example usage
str1 = "101010"
str2 = "11111100000"
result = operator(str1, str2)
print(f"Result of operator on {str1} and {str2} is : {result}")      
