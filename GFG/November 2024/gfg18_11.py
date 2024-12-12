def RotateTheArray(arr,d):
    arr[:d]=reversed(arr[:d])
    arr[d:]=reversed(arr[d:])
    arr[:]=reversed(arr[:])


arr=list(map(int,input("Enter space separate array :").split()))
print(arr)
d=int(input("Enter where from you want to Rotated the array :"))
RotateTheArray(arr,d)
print(arr)