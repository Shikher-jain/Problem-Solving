# Parenthesis Checker

s="{([])}"

s="(()()"
# s="((()"
arr=[]
for i in s:
    # print(i)
    if i =="(":
        arr.append(i)
    if i==")":
        if "(" in arr:
            arr.pop()
    if i =="[":
        arr.append(i)
    if i=="]":
        if "[" in arr:
            arr.pop()
    if i =="{":
        arr.append(i)
    if i=="}":
        if "{" in arr:
            arr.pop()
if not arr:
    # print(arr)
    print(True)
print(False)