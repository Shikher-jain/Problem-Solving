# User function Template for Python3

class Solution:
    def maxLength(self, s):
        left = right = max_length = 0
        
        # Left to right 
        for i in s:
            if i == '(':
                left += 1
            elif i == ')':
                right += 1
            
            if left == right:
                max_length = max(max_length, 2 * right)
            elif right > left:
                left = right = 0
        
        # Right to left scan
        left = right = 0
        for i in reversed(s):
            if i == ')':
                right += 1
            elif i == '(':
                left += 1
            
            if left == right:
                max_length = max(max_length, 2 * left)
            elif left > right:
                left = right = 0

        return max_length

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))

# } Driver Code Ends