# NAVIE STRING MATCHING

def search(pattern, text):
    m = len(pattern)
    n = len(text)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            print(f"Pattern found at index {i}")

if __name__ == "__main__":

    # Example 1
    txt = "AABAACAADAABAABA"
    pat = "AABA"
    print("\nExample 1:")
    search(pat, txt)

    # Example 2
    txt = "agd"
    pat = "g"
    print("\nExample 2:")
    search(pat, txt)
