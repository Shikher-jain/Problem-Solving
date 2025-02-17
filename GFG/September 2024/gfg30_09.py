#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

class Solution:
    def inorder(self,root,item):
        if root:
            self.inorder(root.left,item)
            item.append(root.data)
            self.inorder(root.right,item)
            
    def merge(self, root1, root2):
        item1,item2=[],[]
        self.inorder(root1,item1)    
        self.inorder(root2,item2)    
        return sorted(item1+item2)
        
        
#{ 
 # Driver Code Starts.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == 'N':
        return None
    
    # Creating list of strings from input string after splitting by space
    ip = s.split()
    
    # Create the root of the tree
    root = Node(int(ip[0]))
    
    # Push the root to the queue
    queue = [root]
    
    # Starting from the second element
    i = 1
    while queue and i < len(ip):
        # Get and remove the front of the queue
        currNode = queue.pop(0)
        
        # Get the current node's value from the string
        currVal = ip[i]
        
        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            
            # Push it to the queue
            queue.append(currNode.left)
        
        # For the right child
        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]
        
        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            
            # Push it to the queue
            queue.append(currNode.right)
        i += 1
    
    return root

if __name__ == "__main__":
    s = input()
    root1 = buildTree(s)
    s = input()
    root2 = buildTree(s)
    obj = Solution()
    vec = obj.merge(root1, root2)
    print(" ".join(map(str, vec)))

# } Driver Code Ends