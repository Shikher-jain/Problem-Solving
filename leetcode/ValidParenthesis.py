class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
                # print(stack)
            elif c == '{':
                stack.append('}')
                # print(stack)
            elif c == '[':
                stack.append(']')
                # print(stack)
            elif not stack or stack.pop() != c:
                # print(stack)
                return False
            # print(stack)
        return not stack
# class Solution:
    def isValid1(self, s: str) -> bool:
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
    
obj=Solution()
s1 = "()[]{}"
s2 = "(]"
print(obj.isValid(s1))
# print(obj.isValid(s2))

print(obj.isValid1(s1))
# print(obj.isValid1(s2))