class Solution:
    def rearrange(self, arr):      

        arrP=[]
        arrN=[]

        while arr:
            if arr[0] >= 0:
                arrP.append(arr.pop(0))
            else:
                arrN.append(arr.pop(0))

        while arrP or arrN:
            if arrP:
                arr.append(arrP.pop(0))
            if arrN:
                arr.append(arrN.pop(0))
        print(arrP,"\n",arrN)
        del arrP
        del arrN
        
        return arr
    
# print(arrP)
# print(arrN)


arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
print(arr)
print(Solution().rearrange(arr))