from typing import List
class Solution:
  def threeConsecutiveOdds(self, arr:List[int]) -> bool:
    count = 0
    for a in arr:
      count = count + 1 if a % 2 == 1 else 0
      if count == 3:
        return True
    return False


arr = [1,2,34,3,4,5,7,23,12]
obj=Solution()
print(obj.threeConsecutiveOdds(arr))