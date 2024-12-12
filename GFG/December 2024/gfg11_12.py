class Solution:
    def nextGap(self, gap):
        return 0 if gap <= 1 else (gap // 2) + (gap % 2)

    def mergeArrays(self, a, b):
        n, m = len(a), len(b)
        gap = n + m
        while gap > 0:
            gap = self.nextGap(gap)
            
            i, j = 0, 0
            while i + gap < n:
                if a[i] > a[i + gap]:
                    a[i], a[i + gap] = a[i + gap], a[i]
                i += 1
            j = max(gap - n, 0)
            i = 0 if gap > n else n - gap
            while i < n and j < m:
                if a[i] > b[j]:
                    a[i], b[j] = b[j], a[i]
                i += 1
                j += 1
            j = 0
            while j + gap < m:
                if b[j] > b[j + gap]:
                    b[j], b[j + gap] = b[j + gap], b[j]
                j += 1


a= [2, 4, 7, 10]; b = [2, 3]
obj=Solution()
print(a,b)
print(obj.mergeArrays(a,b))
print(a,b)
# Output:
# 2 2 3 4
# 7 10
