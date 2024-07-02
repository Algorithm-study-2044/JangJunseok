# 4:07시작. 18분. 11분 소요. 1224ms. 67beats.

# road가 두 도시를 연결한다. 그래서 각 도시의 value를 더해준다.
# 그래서 도시 입장에서는, road가 연결한 개수.

from collections import defaultdict

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        freq = {}
        # 이것도 테스트 케이스 고려 안해서 틀렸다. 만약 나머지가 아예 안나와서, 0으로 되어버린다면?
        # 그러면 defaultdict는 이걸 처리해주지 않는다. 그래서 이런 경우에는 0으로 초기화해주는게 좋다.
        for i in range(n):
            freq[i] = 0

        for start,end in roads:
            freq[start] += 1
            freq[end] += 1

        res = 0

        for idx,value in enumerate(sorted(freq.values())):
            res += (idx+1) * value
        return res
            