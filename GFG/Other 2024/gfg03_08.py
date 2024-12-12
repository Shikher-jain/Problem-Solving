#THE CELEBRITY PROBLEM


from collections import defaultdict
class Solution:
    def celebrity(self, mat):
        # code here
        d=defaultdict(list)
        for i in range(len(mat)) :
            for j in range(len(mat)) :  #   traverse whole matrix
                if mat[i][j]==1 :
                    d[j].append(i)
        for i in range(len(mat)) :
            c0=0
            for j in range(len(mat)) :
                if mat[i][j]==0 :
                    c0 +=1
            if c0==len(mat) and len(d[i])==len(mat)-1 :
                return i
        return -1
#{ 
 # Driver Code Starts
# Main function to handle input and output
if __name__ == "__main__":
    t = int(input()) #  TEST CASE
    for _ in range(t):
        n = int(input())
        M = []
        for _ in range(n):
            M.append(list(map(int, input().split())))
    # M =[[0,0,1],
    #     [0,0,0],
    #     [0,0,1]]
    ob = Solution()
    print(ob.celebrity(M))

# } Driver Code Ends


'''
mat[i][j]

i j ka janta hai  means if mat[i][j] = 1
kya j bhi i ko janta hai nested if mat[j][i] = 0

agr nhi toh i celebrity hai
o/w -1 return

''' 