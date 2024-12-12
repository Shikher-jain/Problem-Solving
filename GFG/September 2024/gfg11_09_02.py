import heapq

def minCost(ropes):
    heapq.heapify(ropes)
    total_cost = 0
    while len(ropes) > 1:
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)
        cost = first + second
        total_cost += cost
        heapq.heappush(ropes, cost)
    return total_cost
ropes = [4, 3, 2, 6]
print(f"Minimum cost to connect ropes: {minCost(ropes)}")
