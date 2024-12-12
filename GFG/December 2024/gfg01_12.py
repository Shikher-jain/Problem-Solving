from collections import Counter

class Solution:
    def nonRepeatingChar(self,s):
        
        # --------------------
        # cnt={}
        # for ch in s:
        #     cnt[ch]=ch.get(ch,0) + 1
        
        # --------------------
        cnt=Counter(s)
        
        for ch in s:
            if cnt[ch]==1:
                return ch
        return "$"
    

# import atexit
# import io
# import sys

# _INPUT_LINES = sys.stdin.read().splitlines()
# input = iter(_INPUT_LINES).__next__
# _OUTPUT_BUFFER = io.StringIO()
# sys.stdout = _OUTPUT_BUFFER


# @atexit.register
# def write():
#     sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())




s = str(input())
obj = Solution()
ans = obj.nonRepeatingChar(s)
if (ans != '$'):
    print(ans)
else:
    print(-1)

print("~")
