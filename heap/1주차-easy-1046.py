# 힙은 자식 노드간의 순서를 보장해주지는 않는다.
# 그리고 최대순서 힙 정렬하는거 배움.
# 15분 정도. pass.

import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        heap = []
        for item in stones:
            heapq.heappush(heap,(-item,item))

        while len(heap) > 1:
            val_1 = heapq.heappop(heap)[1]
            val_2 = heapq.heappop(heap)[1]
            diff = val_1 - val_2
            if diff != 0:
                heapq.heappush(heap,(-diff, diff))

        if len(heap) == 1:
            return heap[0][1]
        else:
            return 0