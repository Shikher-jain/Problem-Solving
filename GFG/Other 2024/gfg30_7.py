# RAT IN A MAZE PROBLEM 1

from typing import List

class Solution:
    
    def temp(self,i:int,j:int,a:List[List[int]],n:int,ans:List[str],move:str,v:List[List[int]]):
    
    # def temp(self,i,j,a,n,ans,move,v):
    # v=VISITED
        if i==n-1 and j==n-1:
            ans.append(move)
            return
            
        # D
        if i+1 <n and not v[i+1][j] and a[i+1][j]==1:
            v[i][j]=1
            self.temp(i+1,j,a,n,ans,move + 'D',v)
            v[i][j]=0
            
        # L
        if j-1 >=0 and not v[i][j-1] and a[i][j-1]==1:
            v[i][j]=1
            self.temp(i,j-1,a,n,ans,move + 'L',v)
            v[i][j]=0
            
        # U
        if i-1 >=0 and not v[i-1][j] and a[i-1][j]==1:
            v[i][j]=1
            self.temp(i-1,j,a,n,ans,move + 'U',v)
            v[i][j]=0
            
        # R
        if j+1 <n and not v[i][j+1] and a[i][j+1]==1:
            v[i][j]=1
            self.temp(i,j+1,a,n,ans,move + 'R',v)
            v[i][j]=0
            
            
    def findPath(self, m: List[List[int]]) -> List[str]:
        # code here
        n=len(m[0])
        ans=[]
        v=[ [ 0 for _ in range(n) ] for _ in range(n) ]
        
        if m[0][0]==1:
            self.temp(0,0,m,n,ans,"",v)
        return ans
        
if __name__ == "__main__":
    t = int(input().strip()) #test cases 
    for _ in range(t):
        n = int(input().strip())
        m = []
        for i in range(n):
            m.append(list(map(int, input().strip().split())))
        obj = Solution()
        # m=[
        #     [1, 0, 0, 0],
        #     [1, 1, 0, 0],
        #     [0, 1, 1, 1],
        #     [0, 0, 1, 1]
        #   ]

        result = obj.findPath(m)
        result.sort()
        if len(result) == 0:
            print(-1)
        else:
            print(" ".join(result))

# 1 0 0 0
# 1 1 0 0
# 0 1 1 1
# 0 0 1 1
