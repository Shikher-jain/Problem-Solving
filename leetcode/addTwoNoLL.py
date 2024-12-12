A=[2,4,3]
B=[5,6,4]
string1=""
for i in A[::-1]:
    string1+=str(i)
# print(string1)
string2=""
for i in B[::-1]:
    string2+=str(i)
# print(string2)
print((list(str(int(string1)+int(string2))))[::-1])

# A=int(string1)
# B=int(string2)
# print(A,B,list(str(C))                              )
                                              