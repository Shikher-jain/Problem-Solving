arr=[4,2,7,6,9]  #62
# arr=[4,3,2,6]  #29

ans=0
n=len(arr)
arr.sort()
while len(arr) > 1:
    first = arr.pop(0)
    second = arr.pop(0)
    ans += first + second
    arr.append(first + second)
    arr.sort()
print(ans)
