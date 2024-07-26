# 2:07 시작. 43ms. 60.28% beats.

# 모든 사람을 다 한 도시에 밀어넣고,
# 그러면 거기서 한명을 뺀다고 한다면?
# 두 도시간의 격차는.. 470 vs 0에서.

# 470에서, n개를 뺀다.

# 한번 하면서, 왼쪽꺼를 다 더해주고,
# 상위 n개의 경우에는, -(a-b) 해준다. 

# 시간복잡도는? nlogn + n/2logn -> nlogn.

import heapq
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total = 0
        n = len(costs)
        hp = []
        for a,b in costs:
            total += a
            heapq.heappush(hp,(-(a-b),[a,b]))
        for _ in range(n//2):
            elem = heapq.heappop(hp)[1]
            total -= (elem[0] - elem[1])
        return total