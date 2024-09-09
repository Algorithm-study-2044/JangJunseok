# 7:50

# 왼쪽에는 한번도 등장 x
# 오른쪽에는 모두 등장했어야 함.

# 그러면 오른쪽에 dic 놔두고,
# dic에서 item len이 n과 같은경우
# 그거를 왼쪽 set과 대조.

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        pointed = defaultdict(int)
        start_set = set()
        end_set = set()
        for start, end in trust:
            pointed[end] += 1
            start_set.add(start)
            if pointed[end] == n-1:
                end_set.add(end)
        for cand in end_set:
            if cand not in start_set:
                return cand
        return -1