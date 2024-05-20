# 2:34 . 5분 소요. 545ms. 86.29% beats.

import math
class Solution(object):
    def kClosest(self, points, k):

        def calc_dist((x,y)):
            return math.sqrt(x**2+y**2)
        
        points.sort(key=lambda x:calc_dist(x))

        return points[:k]

# sorting을 사용하면? O(NlogN) 시간복잡도.
    

# 이렇게 하면, O(N * logK) 시간복잡도.
# 힙에 아이템을 추가하거나 pop하는데, O(logK) 시간이 걸림.

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        heap = []
        
        for (x, y) in points:
            dist = -(x*x + y*y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]