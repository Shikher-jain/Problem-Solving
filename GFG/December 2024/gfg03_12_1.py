class Solution:
    def minChar(self, s):
        
        n=len(s)
        revS = s[::-1]
        # $ for mid element
        combined = s + "$" + revS

        lps = [0] * len(combined)
        for i in range(1, len(combined)):
            j = lps[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j += 1
            lps[i] = j

        return n - lps[-1]

if __name__ == "__main__":

    s = input()
    obj = Solution()
    ans = obj.minChar(s)
    print(ans)
    print("~")

