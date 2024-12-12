# # Shortest path in matrix

mat= [
    [9,4,9,9],
    [6,7,6,4],
    [8,3,3,7],
    [7,4,9,10]
    ]


r = len(mat)
c = len(mat[0])
print("Number of rows:", r)
print("Number of column:", c)

dp = [[0 for _ in range(c)] for _ in range(r)]

dp[0][0] = mat[0][0]
for j in range(1, c):
    dp[0][j] = dp[0][j - 1] + mat[0][j]

for i in range(1, r):
    dp[i][0] = dp[i - 1][0] + mat[i][0]

for i in range(1, r):
    
    for j in range(1, c):
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + mat[i][j]

print("The minimum path sum is:", dp[r - 1][c - 1]) 