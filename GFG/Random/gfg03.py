#User function Template for python3

class Solution:
    def getPairs(self, arr):
        # code here
        n=len(arr)
        ans=list()
        for i in range(n):
            for j in range(i+1,n):
                if arr[i]+arr[j]==0:
                    ans.append([arr[i],arr[j]])
                    ans=sorted(list(set(ans[-1])))

        return ans

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr
    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()
if __name__ == "__main__":

    arr = list(map(int, input().strip().split()))

    obj = Solution()
    res = obj.getPairs(arr)
    if len(res) == 0:
        print()
    else:
        IntMatrix().Print(res)

# } Driver Code Ends