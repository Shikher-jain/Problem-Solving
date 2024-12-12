# Find the Minimum and Maximum Number of Nodes Between Critical Points
import math
from typing import Optional,List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        minDistance = math.inf
        firstMaIndex = -1
        prevMaIndex = -1
        index = 1
        prev = head  # Point to the index 0.
        curr = head.next  # Point to the index 1.
    
# middle value ass pass se choti oni chaiye
        while curr.next:
          if curr.val > prev.val and curr.val > curr.next.val or \
            curr.val < prev.val and curr.val < curr.next.val:
            if firstMaIndex == -1:  # Only assign once.
              firstMaIndex = index
            if prevMaIndex != -1:
              minDistance = min(minDistance, index - prevMaIndex)
            prevMaIndex = index
          prev = curr
          curr = curr.next
          index += 1

        if minDistance == math.inf:
          return [-1, -1]
        return [minDistance, prevMaIndex - firstMaIndex]

head = [1,3,2,2,3,2,2,2,7]
obj=Solution()
print(obj.nodesBetweenCriticalPoints(head))