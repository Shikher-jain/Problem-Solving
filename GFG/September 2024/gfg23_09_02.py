# # arr = [1, 2, 4, 4]
# arr = [2,2 ,6 ,7 ,8]

# n = len(arr)
# seen = set()
# B = 0
# for num in arr:
#     if num in seen:
#         B = num
#     seen.add(num)


# total_sum = n * (n + 1) // 2  
# actual_sum = sum(arr) - B  

# A =total_sum - actual_sum

# print("B:", B)
# print("Aing:", abs(A))





# # class Solution:
# #     def findAingAndB(self, arr):
# #         n = len(arr)
        
# #         # To find the B
# #         seen = set()
# #         B = 0
# #         for num in arr:
# #             if num in seen:
# #                 B = num
# #             seen.add(num)
        
# #         # To find the Aing number using sum formula
# #         total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
# #         actual_sum = sum(arr) - B  # Sum of array minus the B
        
# #         # The Aing number is the difference between the expected sum and actual sum
# #         A = total_sum - actual_sum
        
# #         # Return as tuple (Aing, B)
# #         return (A, B)

# # # Example usage:
# # arr = [2, 2, 6, 7, 8]
# # sol = Solution()
# # result = sol.findAingAndB(arr)
# # print("Aing:", abs(result[0]))
# # print("B:", result[1])

class Solution:
    def findAingAndB(self, arr):
        n = len(arr)
        seen = set()
        B = 0
        i=0
        for num in arr:
            if num in seen:
                B = num
            seen.add(num)
            
        # for i in range(n):
        arr.sort()
        for i in  range(1,max(arr)+1):
            if i not in arr:
                A=i
                break

        return [B,A]
arr = [2, 2, 6, 7, 8]
# arr=[2,2]
sol = Solution()
result = sol.findAingAndB(arr)
print("A:", result[0])
print("B:", result[1])

'''
# a1=(list( x for x in range(1,max(arr)+1 )))
arr.sort()
for i in  range(1,max(arr)+1):
    if i not in arr:
        print(i)
        break

        
class Solution:
    def findTwoElement( self,arr): 
        n = len(arr)
        seen = set()
        B = 0
        A=0
        for num in arr:
            if num in seen:
                B = num
            seen.add(num)
            
        arr.sort()
        for i in  range(1,max(arr)+2):
            if i not in arr:
                A=i
                break
        
        return [B,A]
        


        
        '''