class Solution:
    def passThePillow(self, n: int, time: int) -> int:
    # Repeat every (n - 1) * 2 sec.
        time %= (n - 1) * 2
        # print(time)           #-----
        if time < n:  # Go forward 1.
            return 1 + time
        # return n - (time - (n - 1))  # Go backward from n.
        return 2*n - time - 1  # Go backward from n.

obj=Solution()
print(obj.passThePillow(4,5))
print(obj.passThePillow(3,2))
print(obj.passThePillow(18,38))