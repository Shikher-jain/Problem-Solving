arr=[1, 2, 3, 2, 1]
n=len(arr)
single = 0
for i in range(n):
    print("1",single,",",arr[i])
    single = single ^ arr[i]
    print("2",single,",",arr[i])
print( single)