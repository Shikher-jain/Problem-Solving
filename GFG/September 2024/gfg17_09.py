arr= [3, 9, 12, 16, 20]
k=3
# arr= [1, 5, 8, 10]
# k=2

# arr= [1, 8, 10, 6 ,4 ,6 ,9 ,1]
# k=7

arr=[2, 4, 3, 9 ,9, 10, 9, 7, 1, 2]
k=4

t=len(arr)
print(arr)
i=0
while t:
    # if i<k-1:
    if arr[i]-k <= 0 and arr[i]-k < k:
        arr[i]+=k
    else:
        arr[i]-=k
    t-=1
    i+=1
print(arr)
print(max(arr)-min(arr) )
