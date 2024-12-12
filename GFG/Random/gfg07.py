def fx(arr,k):
    print(arr)
    
    if len(arr)<=k:
        return arr[::-1]
    return (arr[k-1::-1]+arr[len(arr):k-1:-1])
        
arr=[1,2,3,4,5]
print(fx(arr,7)) 
print(fx(arr,3)) 