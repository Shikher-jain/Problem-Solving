s="(()()"
s="((()"
arr=[]
a=0
for i in s:
    print(i)
    if i =="(":
        arr.append(i)
    if i==")":
        if "(" in arr:
            a+=1
            arr.pop()

print(a*2)
print(arr)