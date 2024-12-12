# Minimum Difference Between Largest and Smallest Value in Three Moves
from typing import List
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # n = len(nums)
        if len(nums) < 5:
            return 0
        nums.sort()
        # ans = math.inf  #we also used this 
        ans=nums[-1]-nums[0]
    # now nums is sort
    # now change last three maximum to nums[0]
    # then return the max in nums
        for i in range(4):
            ans = min(ans, nums[len(nums) - 4 + i] - nums[i])
        return ans
  
nums = [1,5,0,10,14]
obj=Solution()
print(obj.minDifference(nums))