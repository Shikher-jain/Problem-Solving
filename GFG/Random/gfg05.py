def duplicate(n ,arr):
    # code here
    
    arr1=list(set(arr))
    m=len(arr1)
    if n == m:
        return [-1]
    while n:  
        arr.pop(arr1.index(arr1[0]))
        n-=1
    arr=list(set(arr))
    arr.sort()
    return arr

arr = [2,3,1,1,2,3]
print(duplicate(len(arr),arr))  