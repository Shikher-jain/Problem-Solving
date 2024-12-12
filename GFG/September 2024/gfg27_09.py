def f(k,arr):
    n=len(arr)
    if n * k == 0:
        return []
    if k == 1:
        return arr
    for i in range(n-k+1):
        arr.append(max(arr[i:i+k]))
    return arr[n:]

k=3
arr=[1,2,3,1,4,5,2,3,6]
k=4
arr=[8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
print(f(k,arr))