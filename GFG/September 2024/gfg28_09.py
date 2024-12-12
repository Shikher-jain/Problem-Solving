k = 3; arr= [10, 30, 40, 50, 20]

# n = len(arr)
dp = [float('inf')] * len(arr) # Initialize dp array with a large value
dp[0] = 0  # no cost on Ist stone

for i in range(1, len(arr)):
    # Check i-k to i-1
    for j in range(1, k+1):
        if i - j >= 0:  
            dp[i] = min(dp[i], dp[i-j] + abs(arr[i] - arr[i-j]))


print( dp[-1] ) 

