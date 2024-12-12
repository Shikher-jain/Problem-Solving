# x= -123
# rev=0
# if x>=0:
#     while x != 0:
#         a=x%10
#         rev=rev*10+a
#         x//=10
# else:
#     x=-x
#     print(x)
#     while x != 0:
#         a=x%10
#         rev=rev*10+a
#         x//=10
#     rev=-rev
# print(rev)

# --------------------------------------

class Solution:
    def reverse(self, x: int) -> int:
        print(x)
        str_x = str(x)
        if x < 0:
            str_x = str_x[1::]
            result = int(f'-{str_x[::-1]}')
        else:
            result = int(str_x[::-1])
        if result < -2 ** 31 or result > 2 ** 31 - 1:
            return 0
        return result
sol=Solution()
ans=sol.reverse(-123)
print(ans)