def min_cost_to_reach_last_stone(arr, k):
    n = len(arr)
    dp = [float('inf')] * n  # Initialize dp array with a large value
    dp[0] = 0  # Base case: no cost to stand on the first stone
    
    for i in range(1, n):
        # Check all jumps from i-k to i-1
        for j in range(1, k+1):
            if i - j >= 0:  # Make sure i-j is a valid index
                dp[i] = min(dp[i], dp[i-j] + abs(arr[i] - arr[i-j]))
    
    print( dp[n-1])  # The minimum cost to reach the last stone
    print( dp[-1] ) # The minimum cost to reach the last stone

k = 3; arr= [10, 30, 40, 50, 20]
min_cost_to_reach_last_stone(arr, k)