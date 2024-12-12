a= [2, 4, 7, 10]; b = [2, 3]
print(a,b)

n,m=len(a),len(b)
i,j=n-1,0

while( j<m and i>=0 ):
    if a[i]<b[j]:break

    a[i],b[j]=b[j],a[i]
    i-=1
    j+=1

print(a,b)
a.sort()
b.sort()
print(a,b)