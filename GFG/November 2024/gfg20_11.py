class Solution:
    def findMajority(self, arr):
        num1, num2, c1, c2 = None, None, 0, 0
        n = len(arr)
        for x in arr:
            if x == num1:
                c1 += 1
            elif x == num2:
                c2 += 1
            elif c1 == 0:
                num1 = x
                c1 = 1
            elif c2 == 0:
                num2 = x
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        c1, c2 = 0, 0
        for x in arr:
            if x == num1:
                c1 += 1
            elif x == num2:
                c2 += 1
        res = []
        if c1 > n // 3:
            res.append(num1)
        if c2 > n // 3:
            res.append(num2)
        res.sort()
        return res