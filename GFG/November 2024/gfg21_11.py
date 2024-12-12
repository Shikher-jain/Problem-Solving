from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        gain=0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                gain += prices[i] - prices[i-1]
        return gain 


arr = list(map(int, input().strip().split()))
solution = Solution()
res = solution.maximumProfit(arr)
print(res)  
