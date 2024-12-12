def longestPrefixSuffix(s):
    n = len(s)
    lps = [0] * n  # LPS array to store the longest prefix suffix values
    length = 0  # Length of the previous longest prefix suffix
    i = 1
    
    # Build the LPS array
    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # Fallback to the length of the previous longest prefix suffix
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    # The last value in the LPS array contains the result
    return lps[-1]


s = "abab"
result = longestPrefixSuffix(s)
print("Length of the longest proper prefix which is also a proper suffix:", result)
