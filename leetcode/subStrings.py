def longestSubstring(s):
    char_set = set()
    left = 0
    longest = 0
    # print(s)
    # print(char_set)
    # print(len(s))
    for right in range(len(s)):
        print(s[right] in char_set)
        while s[right] in char_set:
            print(char_set)
            print(s[right])
            char_set.remove(s[left])
            print(char_set)
            # print(s[right])
            left += 1
        char_set.add(s[right])
        longest = max(longest, right - left + 1)
    
    return longest

# print(longestSubstring("abcabcbb"))  
# print(longestSubstring("bbbbb"))     
print(longestSubstring("pwwkew"))    
# print(longestSubstring(""))          
# print(longestSubstring("dvdf"))      
