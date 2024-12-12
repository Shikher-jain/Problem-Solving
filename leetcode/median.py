nums1=[1,3]
nums2=[2]
nums3=(nums1+nums2)
nums3.sort()
print(nums3)
# print(len(nums3))
if (len(nums3) % 2==0):#even
    print(  (nums3[(len(nums3)//2)]  + nums3[(len(nums3)//2 -1)] )/2 )
    # return (  (nums3[(len(nums3)//2)]  + nums3[(len(nums3)//2 -1)] )/2 )
else:
    print(  float(nums3[(len(nums3)//2)]))
    # return float((nums3[(len(nums3)//2)]))

# ---------------------------------------------------------------

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         mn = (len(nums1)+len(nums2))
#         if mn%2 == 1:
#             mn = mn//2
#             i = 0
#             while i <= mn:
#                 try:
#                     if nums1[-1] >= nums2[-1]:
#                         x = nums1.pop()
#                     else:
#                         x = nums2.pop()
#                     i += 1
#                 except:
#                     break

#             while i <= mn and nums1 != []:
#                 x = nums1.pop()
#                 i += 1
#             while i <= mn and nums2 != []:
#                 x = nums2.pop()
#                 i += 1
#             return x
#         else:
#             mn = mn//2
#             i = 0
#             while i < mn:
#                 try:
#                     if nums1[-1] >= nums2[-1]:
#                         x = nums1.pop()
#                     else:
#                         x = nums2.pop()
#                     i += 1
#                 except:
#                     break

#             while i < mn and nums1 != []:
#                 x = nums1.pop()
#                 i += 1
#             while i < mn and nums2 != []:
#                 x = nums2.pop()
#                 i += 1
#             if nums1 == []:
#                 return (x+nums2.pop())/2
#             if nums2 == []:
#                 return (x+nums1.pop())/2
#             if nums2[-1] > nums1[-1]:
#                 return (x+nums2.pop())/2
#             return (x+nums1.pop())/2

# sol=Solution()
# sols=sol.findMedianSortedArrays(nums1=[1,3],nums2=[2])
                