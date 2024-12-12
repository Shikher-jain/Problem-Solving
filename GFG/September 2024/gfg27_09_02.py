k=4
arr=[8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
def f(k,arr):
    n = len(arr)
    if n == 0 or k == 0:
        return []
    if k == 1:
        return arr

    dq = []  
    result = []

    for i in range(n):
        # Remove elements that are out of the current window
        if dq and dq[0] < i - k + 1:
            dq.pop(0)
        
        # Remove all elements smaller than the current element (they are not useful anymore)
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        
        # Add current element index to the list (acting as deque)
        dq.append(i)
        
        # Start adding the max to the result after the first window is processed
        if i >= k - 1:
            result.append(arr[dq[0]])  # The element at the front is the max of the current window

    return result

k=4
arr=[8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
print(f(k,arr))