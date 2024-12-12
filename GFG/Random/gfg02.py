class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        arr=list(set(arr))
        if len(arr)<2:
            return -1
        arr.sort()        
        return arr[-2]

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    ob = Solution()
    ans = ob.getSecondLargest(arr)
    print(ans)
