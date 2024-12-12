k=3
arr= [5, 8, 10, 13]


Tcount=0
for i in arr:
    count=i//k
    if i%k!=0:
        count+=1
    Tcount+=count
print(Tcount)