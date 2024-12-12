def Fx(arr):
    print(arr)
    arr.sort()
    print(arr)
    print(len(arr),len(arr[0]))

    for i in range(1,len(arr)):
        print(arr[i][0],arr[i-1][1])
        if arr[i][0] < arr[i-1][1]:
            return False
        return True

arr=[
    [1,4],
    [10,15],
    [7,10]
]
print(Fx(arr))