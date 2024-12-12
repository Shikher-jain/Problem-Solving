def rev():
    A=["h","e","l","l","o"]
    ss=A[::-1]
    return(ss)
# print(rev())

def rev1():
    A1=[]
    A=["h","e","l","l","o"]
    for i in A[::-1]:
        A1.append(i)
    print(A1)
# rev1()

def rev2(s):
    l = 0
    r = len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s
A=["h","e","l","l","o"]
print(rev2(A))