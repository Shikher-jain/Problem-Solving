def is_balanced(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    
    stack = []
    # print(pairs.values())     #dict_values(['(', '[', '{'])
    # print(pairs.keys())       #dict_keys  ([')', ']', '}'])
    for char in s:
        if char in pairs.values():
            #opening bracket
            print(char)
            stack.append(char)

        elif char in pairs.keys():
            #closing bracket
            if stack and stack[-1] == pairs[char]:
                print(char)
                print(stack , stack[-1] ,pairs[char])
                stack.pop()
            else:
                return False
    
    # If stack is empty, all brackets are balanced
    return not stack


s = input("Enter a string containing parentheses, brackets, or curly braces: ")
print(is_balanced(s))
