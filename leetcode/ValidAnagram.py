s="anagram"
t="nagaram"

                # 1
                
# if len(s)==len(t):
#     s=list(s)
#     t=list(t)
#     t.sort()
#     s.sort()
#     if(s==t):
#         print(True)
#     else:
#         print(False)
# else:
#     print(False)

                # 2

# s=list(s)
# t=list(t)
# t.sort()
# s.sort()
# print(s==t)

                #3

from collections import Counter
# Keeps 2 counters for each string
# Compare the counters
print( Counter(s) == Counter(t))