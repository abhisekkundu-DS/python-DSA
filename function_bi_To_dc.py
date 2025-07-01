def function(abc):
    decimal = 0
    for i in range(len(abc)):
        ans = int(abc[i]) * (2**(len(abc)-i-1)) 
        decimal = decimal + ans
    return decimal
# Example usage
abc = "1101"
decimal_representation = function(abc)
print(f"Decimal representation of {abc} is: {decimal_representation}")
