class Solution:
    def findMajority(self, nums):
        n = len(nums)
        if n == 0:
            return [-1]  
        elif n<=3:
            return list(set(nums))

        num1, num2 = None,None
        c1, c2 = 0, 0
        
        for x in nums:
            if x == num1:
                c1 += 1
            elif x == num2:
                c2 += 1
                
                
            elif c1 == 0:
                num1 = x
                c1 = 1
            elif c2 == 0:
                num2 = x
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        
        c1, c2 = 0, 0
        for x in nums:
            if x == num1:
                c1 += 1
            elif x == num2:
                c2 += 1
        
        res = []
        if c1 > n // 3:
            res.append(num1)
        if c2 > n // 3:
            res.append(num2)
        
        # if not res:
        #     res.append(-1)  
        
        return res if res else [-1]

s = input().strip()
nums = list(map(int, s.split()))
ob = Solution()
ans = ob.findMajority(nums)
print(" ".join(map(str, ans)))
