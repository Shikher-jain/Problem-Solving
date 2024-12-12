class Solution:
    def missingNumber(self,arr):
        n = len(arr)

        j = 0        
        for i in range(n):
            if arr[i] <= 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1  #negative 0 se j-1 tk
        
        arr = arr[j:] #positive j se last tk
        n = len(arr)
        
        
        for i in range(n):
            val = abs(arr[i])
            if 1 <= val <= n:
                arr[val - 1] = -abs(arr[val - 1]) 
        
        
        for i in range(n):
            if arr[i] > 0:
                return i + 1  # first missing positive
        return n + 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    arr = [int(x) for x in input().strip().split()]
    ob = Solution()
    print(ob.missingNumber(arr))


if __name__ == "__main__":
    main()
