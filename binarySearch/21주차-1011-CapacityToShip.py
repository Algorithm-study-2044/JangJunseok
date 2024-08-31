# 384ms. 71.67% beats.

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 최소값은, 이렇게 하면 지금값과 max(weights) 사이에 값들이 되어버릴 수도.
        # l = math.ceil(sum(weights) / days)
        l = max(weights)
        r = sum(weights)

        def can_traverse(cargo,days):
            dt = 0
            curr = 0
            for i in weights:
                if curr + i <= cargo:
                    curr += i
                else:
                    dt += 1
                    curr = i
            # 마지막날을 빼먹었다.
            dt += 1
            return True if dt <= days else False
                

        while l <= r:
            mid = (l+r) // 2
            if can_traverse(mid,days):
                r = mid - 1
            else:
                l = mid + 1
        
        return l