from heapq import heappush, heappop

class Solution:
    def jobSequencing(self, d, p):
        jobs = sorted(zip(d, p))
        pq = []

    
        for deadline, profit in jobs:
            if len(pq) < deadline:
                heappush(pq, profit)
            elif pq and pq[0] < profit:
                heappop(pq)
                heappush(pq, profit)

        return [len(pq), sum(pq)]



deadline = list(map(int, input().strip().split()))
profit = list(map(int, input().strip().split()))

obj = Solution()
ans = obj.jobSequencing(deadline, profit)
print(ans[0], ans[1])
print("~")
