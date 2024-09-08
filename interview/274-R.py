# 11:32 시작.
# 이진탐색으로 풀어야할까?
# at least k라는것도 이진탐색이고, h val 찾는것도 이진탐색이다. 

# 만약 딱 맞는게 없었다고 하면, 뭘 반환히야하지?
# 나는 end라고 생각. 왜냐하면. 없을때는 안되는거니까.

# 그런데...[1],[0], [11,15]에서 막힘. 왜?
# 11, 15 사이의 값에서 찾는건가? 아니다. 왜냐하면, 10이 되어야 하는게 아니라, 최대 두개가 되어야 하기 때문이다.

# 그래서 마지막에 min(len(arr1),end)를 해줬음. 만약 적어서 계속 end값이 축소되었을때, end값은 start - 1이 될 수도 있는데,
# 그 보다는 len(arr1)이 되어야 하기 때문...이라고 생각은 하는데,
# 잘 모르겠다. 

from bisect import bisect_left

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        arr1 = sorted(citations)

        # len - bisect_left가 
        def count_at_least(num,arr):
            return len(arr) - bisect_left(arr,num)
        
        start = min(arr1)
        end = max(arr1)

        while start <= end:
            mid = (start + end) // 2
            val = count_at_least(mid,arr1)
            if val == mid:
                return mid
            if val > mid:
                start = mid + 1
            if val < mid:
                # 이러면 기준을 좀 낮춰야.
                end = mid - 1
        
        return min(len(arr1),end)                                      