curr = 0
wait = 0
customers=[[1,2],[2,5],[4,3]]
#          (A,D)

for c in customers:
    # print(c[1])
    curr = max(curr, c[0]) + c[1]
    wait += curr - c[0]
    print(wait)
print(wait / len(customers))  #ans

