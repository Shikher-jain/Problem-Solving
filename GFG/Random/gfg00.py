arr=[1,5, 7, 9, 1, 10, 2]
n=len(arr)
arr1=arr
arr1.sort()
print(  arr.pop(arr1.index(arr1[n-1]))  )


def solve(arr):
    n=len(arr)
    if n == 1:
        return 0
    
    # Binary search approach
    low, high = 0, n - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # Check if the middle element is a peak element
        if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == n - 1 or arr[mid] >= arr[mid + 1]):
            return mid
        # If the element to the right is greater, search the right half
        elif mid < n - 1 and arr[mid] < arr[mid + 1]:
            low = mid + 1
        # If the element to the left is greater, search the left half
        else:
            high = mid - 1

print(solve(arr))