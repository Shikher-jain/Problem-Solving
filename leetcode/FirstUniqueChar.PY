# First Unique Character in a String
import collections
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        # print(count)
        for i, c in enumerate(s):
            # print(i , c)
            if count[c] == 1:
                return i
        return -1

# class Solution:
    def firstUniqChar1(self, s: str) -> int:
        l = Counter(s)
        for i,j in l.items():
            if j==1: 
                return s.index(i)
        return -1

s="loveleetcode"
obj=Solution()
print(obj.firstUniqChar(s))
print(obj.firstUniqChar1(s))