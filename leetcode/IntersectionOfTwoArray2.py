from typing import List,collections

class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    if len(nums1) > len(nums2):
      return self.intersect(nums2, nums1)

    ans = []
    count = collections.Counter(nums1)
    print(count)
    for num in nums2:
      if count[num] > 0:
        ans.append(num)
        count[num] -= 1

    return ans

nums1=[1,2,2,1]
nums2=[2,2]
obj=Solution()
print(obj.intersect(nums1,nums2))