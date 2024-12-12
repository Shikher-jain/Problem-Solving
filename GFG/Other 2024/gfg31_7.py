# LONGEST COMMON PREFIX OF SRTINGS

#User function Template for python3

class Solution:
    def longestCommonPrefix(self, a):
        s=len(a)
        if s==0:
            return ""
        if s==1:
            return a[0]
        
        a.sort()
        
        t=min( len(a[0]) , len(a[s-1]) )
        i=0
        if not(a[0][i]==a[s-1][i] ):
            return -1
        while( t>1 and a[0][i]==a[s-1][i] ):
            i+=1
        
        return a[0][:i]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends