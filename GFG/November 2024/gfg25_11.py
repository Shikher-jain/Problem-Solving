class Solution:
    def maxProduct(self,arr):
        MaxPro=arr[0];Min=arr[0];Max=arr[0]
		
        for i in range(1,len(arr)):
            if arr[i] < 0:
                   Min, Max=Max, Min 
            Max=max(arr[i],arr[i] * Max)
            Min=min(arr[i],arr[i] * Min)
            MaxPro=max(MaxPro,Max)
        return MaxPro


arr=[-2,6,-3,-10,0,3]
print(Solution().maxProduct(arr))

class Solution:
    def maxProduct(self, arr):
        MaxPro = arr[0]
        Min = arr[0]
        Max = arr[0]
        
        for i in range(1, len(arr)):
            if arr[i] < 0:
                Min, Max = Max, Min  # Swap Min and Max
            
            Max = max(arr[i], arr[i] * Max)  # Update Max
            Min = min(arr[i], arr[i] * Min)  # Update Min
            
            MaxPro = max(MaxPro, Max)  # Update MaxPro
        
        return MaxPro


arr = [-2, 6, -3, -10, 0, 3]
print(Solution().maxProduct(arr))
