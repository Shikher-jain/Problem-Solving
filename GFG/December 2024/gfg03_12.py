class Solution:
    def minChar(self, s):
        #Write your code here
        
        n=len(s)
        left,right,miss=0,n-1,n-1
        
        while left < right :
            if s[left] == s[right]:
                left+=1
                right-=1
            
            else:
                miss-=1
                left=0
                right = miss
            
        return n-1-miss


if __name__ == "__main__":

    s = input()
    obj = Solution()
    ans = obj.minChar(s)
    print(ans)
    print("~")

