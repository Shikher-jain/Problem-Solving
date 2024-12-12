
def app1(s):
    print(s)
    # s=s.strip()
    print(s)
    s=int(s)
    print(s)

# s= "-"   failed

def app2(s):
    
    i=0
    while i<len(s) and s[i]==" ":
        i+=1
    # sign = 1
    print(i)

    sign = 1
    # if i<len(s) and (s[i]=="-" or s[i]=="+"):
    if i<len(s):
        sign =-1 if s[i]=="-" else 1
        i+=1
    print("sign:", sign)

    res=0
    while i<len(s) and '0'<=s[i]<='9':
        res = res * 10 +(ord(s[i]) - ord("0")) # ord("0")=48
        i+=1
        
        if res * sign > 2**31 - 1: return 2**31 - 1
        if res * sign < -2**31 : return -2**31

    return ("res :",res * sign)


s="   -123"

# app1(s)
print(app2(s))

# for i in s: 
#     if '0'<=i<='9':
#         print(i)
# print(ord('0'))