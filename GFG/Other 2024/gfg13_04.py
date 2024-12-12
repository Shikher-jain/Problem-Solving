
x = 1
ans = 0
for i in range(32):
    ans = (ans << 1) | (x & 1)
    x >>= 1  
    print( x,",",ans)
print( ans)