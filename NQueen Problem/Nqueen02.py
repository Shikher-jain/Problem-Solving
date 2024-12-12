class Solution:
    def nQueen(self, n):
        def solve(c, row):
            if c == n:
                self.result.append([r + 1 for r in row])
                return
            for r in range(n):
                if all(row[prev] != r and abs(row[prev] - r) != abs(prev - c) for prev in range(c)):
                    row[c] = r
                    solve(c + 1, row)
        
        self.result = []
        solve(0, [0] * n)
        return self.result
        
n = int(input())
ob = Solution()
ans = ob.nQueen(n)
if(len(ans) == 0):
    print("-1")
else:
    for i in range(len(ans)):
        print("[",end="")
        for j in range(len(ans[i])):
            print(ans[i][j],end = " ")
        print("]",end = " ")
    print()
x