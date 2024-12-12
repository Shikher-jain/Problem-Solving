from typing import *
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=(list(set(nums)))
        nums.sort()
        if len(nums)>=3:
            return nums[len(nums)-3]
        return nums[1] if len(nums)==2 else nums[0]
            
obj=Solution()
A=[3,2,1]
B=[2,1]
C=[2,2,3,1]
print(obj.thirdMax(A))
print(obj.thirdMax(B))
print(obj.thirdMax(C))