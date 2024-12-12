str=48
str=46

s=int(str)%10
if 5<s<10:  #6,7,8,9
    ans=str + 10 -s
else:
    ans=str-s

print(ans)
print(s)


class Solution:
    def roundToNearest(self, num_str: str) -> str:
        n = len(num_str)
        if n == 0:
            return num_str  
        last_digit = int(num_str[-1])  
        if last_digit <= 5:
            return num_str[:-1] + '0'  
        else:
            num_str = num_str[:-1] + '0'  
            i = n - 2
            while i >= 0:
                if num_str[i] != '9':
                    return num_str[:i] + chr(ord(num_str[i]) + 1) + num_str[i + 1:]  
                num_str = num_str[:i] + '0' + num_str[i + 1:]  
                i -= 1
            return '1' + num_str  

num_str = input()
ob = Solution()
res = ob.roundToNearest(num_str)
print(res)