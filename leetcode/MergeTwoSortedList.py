list1 = [1,2,4]
list2 = [1,3,4]
# list3=list1+list2
# list3.sort()
# print(list3)

# class ListNode:
class Solution:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def mergeTwoLists(self, list1,list2):
        if not list1 or not list2:
            return list1 if list1 else list2
        if list1.val > list2.val:
            list1, list2 = list2, list1
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
obj=Solution()
print(obj.mergeTwoLists(list1,list2))