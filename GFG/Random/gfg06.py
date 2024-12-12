
class Solution:
    def countPalindromicSubstrings(self, s : str, k : int) -> int:
        # code here
        def Ispalindrome(str):
            return str[:]==str[::-1]
            
        cnt=0
        i=0
        for i in range(len(s)-k+1):
            if Ispalindrome(s[i:i+k]):
                print(s[i:k])
                cnt+=1
        return cnt

s = (input())

k = 2

# k = int(input())
obj = Solution()
res = obj.countPalindromicSubstrings(s, k)

print(res)
