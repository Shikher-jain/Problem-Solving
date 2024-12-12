# linked list pallindrome
	# Return Type: boolean , no need to print just return True or False.

	# {
	# 	# Node Class
	# 	class Node:
	# 	    def __init__(self, data):   # data -> value stored in node
	# 	        self.data = data
	# 	        self.next = None
	# }

class Solution:
    def isPalindrome(self, head):
        d=[]
        head1=head
        while head1:
            d.append(head1.data)
            head1=head1.next
        print(d)
        print( d , d[::-1])
        if d == d[::-1]:
            return True
        return False


#{ 
 # Driver Code Starts
#main


class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to prit the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print("")


if __name__ == '__main__':
    # t = int(input())
    # while (t > 0):
    llist = LinkedList()
    values = input().strip().split()
    for i in reversed(values):
        llist.push(i)
    flag = Solution().isPalindrome(llist.head)
    if flag:
        print("true")
    else:
        print("false")
        # t -= 1
# Contributed by: Harshit Sidhwa

# } Driver Code Ends