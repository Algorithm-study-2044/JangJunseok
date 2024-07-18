# 7:01 시작.
# 4분 소요. 65ms. 15.37% beats. 다른 풀이도 알아볼 것.

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        return [x for x in sorted(list(set(words)),key=lambda x:(-cnt[x],x))][:k]


# lexical은 아니라도 이렇게 할 수도 있지 않을까?

from heapq import heappushpop, heappush
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        n = Counter(words)
        heap = []
        for i in set(words):
            if len(heap) >= k:
                heappushpop(heap,(n[i],i))
            else:
                heappush(heap,(n[i],i))
        
        return [x[1] for x in heap]