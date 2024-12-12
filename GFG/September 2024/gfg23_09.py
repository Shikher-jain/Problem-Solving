# arr=[1,2,4,5]
arr=[13, 33, 43, 16, 25, 19, 23, 31, 29, 35, 10, 2, 32, 11, 47, 15, 34, 46, 30, 26, 41, 18, 5 ,17, 37, 39, 6 ,4 ,20, 27, 9 ,3 ,8, 40, 24, 44, 14, 36, 7, 38 ,12, 1, 42, 12 ,28 ,22,45]
arrS=list(set(arr))
# print(arr)
# print(arrS)
arr.sort()
arrS.sort()
n=len(arr)
i=0
miss=1
duplicate=1
if arr==arrS:
    print(0,0)
while n:
    if arr[i] not in arrS:
        duplicate=arr[i]
        # n-=1
        # i+=1
        break
    else:
        arrS.pop(0)
    
    if len(arr)-n+1 not in arr:
        miss = [len(arr)-n+1]
    n-=1
    i+=1

print("duplicate : ",duplicate)
print("miss : ",miss)
