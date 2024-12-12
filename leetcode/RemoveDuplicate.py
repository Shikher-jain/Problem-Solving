from typing import *
# class Solution:
#     def removeDuplicates(self, nums):
#         # for i in range(len(nums)-len(set(nums))):
#         #     nums=list(set(nums))
#         #     nums.append("_")
#         # return nums
#         return list(set(nums))

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if i < 1 or num > nums[i - 1]:
                nums[i] = num
            i += 1
        return i

A=[1,1,2]
obj=Solution()
print(obj.removeDuplicates(A))