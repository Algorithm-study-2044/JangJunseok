# 7:53 시작. 8:20. 27분 소요.
# 800ms.75% beats.

# 그런데 l을 쓸건지, r을 쓸건지, l<=r이 맞는지. 이런거 계산하는거에서 좀 해멨다.
# 2개,3개 있을때를 두어서, 일반화를 해보자는 것이다.

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # 처음에 일단 꽃개수 충분한지 확인.
        n = len(bloomDay)
        if n < m*k:
            return -1

        l = 0 
        r = n-1
        days = sorted(bloomDay)

        while l <= r:
            mid = (l+r) // 2
            combo = 0
            curr = 0
            curr_day = days[mid]

            for fl in bloomDay:
                if fl <= curr_day:
                    curr += 1
                else:
                    curr = 0
                if curr >= k:
                    curr = 0
                    combo += 1
            
            if combo < m:
                l = mid + 1
            else:
                r = mid - 1
            
        return days[l]