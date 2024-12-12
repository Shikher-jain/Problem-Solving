from collections import defaultdict

def smallestWindow( s, p):
    if len(p) > len(s):
        return "-1"

    FreqP = defaultdict(int)
    for char in p:
        FreqP[char] += 1

    req, ch = len(FreqP), 0

    FreqS = defaultdict(int)

    left, right, min, start = 0, 0, float('inf'), -1

    while right < len(s):
        FreqS[s[right]] += 1

        if s[right] in FreqP and FreqS[s[right]] == FreqP[s[right]]:
            ch += 1

        while ch == req:
        
            if right - left + 1 < min:
                min, start = right - left + 1, left
            FreqS[s[left]] -= 1
        
            if s[left] in FreqP and FreqS[s[left]] < FreqP[s[left]]:
                ch -= 1
            left += 1

        right += 1

    return s[start:start + min] if start != -1 else "-1"

# Example usage:

s = "timetopractice"
p = "toc"
s="mpsbqedzsqyskjqydomdanqfmtqri"
p="rrbqrnbbzyijnwfnimshbjimbfe"
print(smallestWindow(s, p))

