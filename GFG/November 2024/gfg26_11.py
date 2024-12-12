def Carr(arr):
    def kadane(arr):
        max1=0
        max2=float('-inf')

        for n in arr:
            print(max1,max2)
            max1=max(max1+n,n)
            max2=max(max1,max2)
        print(max1,max2)
        print("------------------------------")
        return max2

    maxK=kadane(arr)
    Tsum=sum(arr)
    InvArr=[-n for n in arr]
    maxI=kadane(InvArr)
    print("Total Sum:",Tsum)
    maxC=Tsum + maxI
    return max(maxK,maxC) if maxC!=0 else maxK


arr=[-8,8,9,-9,10,-11,12]
arr=[-1,40,-14,7,6,5,-4,-1]
print(Carr(arr))