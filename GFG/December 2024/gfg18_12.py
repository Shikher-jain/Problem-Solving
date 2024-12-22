def is_possible(arr, k, mid):
    total = 0
    student = 1
    for x in arr:
        total += x
        if total > mid:
            student += 1
            total = x
    return student <= k

def find_pages(arr, k):
    if k > len(arr):
        return -1
    total_sum = 0
    mx = float('-inf')
    for x in arr:
        total_sum += x
        mx = max(mx, x)
    low = mx
    high = total_sum
    ans = float('inf')
    
    while low <= high:
        mid = (low + high) // 2
        if is_possible(arr, k, mid):
            high = mid - 1
            ans = min(ans, mid)
        else:
            low = mid + 1
            
    return ans


arr = [12, 34, 67, 90]
k = 2
ans=find_pages(arr,k)
print(ans)