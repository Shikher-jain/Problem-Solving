#User function Template for python3

class Solution:
    def search(self,arr,key):
        # Complete this function
        low, high = 0, len(arr) - 1
        
        while low <= high:
            # mid = (low + high) // 2
            mid = low + (high - low) // 2

            if arr[mid] == key:
                return mid
            
            if arr[low] <= arr[mid]:
                if arr[low] <= key < arr[mid]:  # Key is in the left half
                    high = mid - 1
                else:  # Key is in the right half
                    low = mid + 1
            else:  # If the right half is sorted
                if arr[mid] < key <= arr[high]:  # Key is in the right half
                    low = mid + 1
                else:  # Key is in the left half
                    high = mid - 1
        
        return -1


A = list(map(int, input().strip().split()))
k = int(input())
ob = Solution()
print(ob.search(A, k))
print("~")

