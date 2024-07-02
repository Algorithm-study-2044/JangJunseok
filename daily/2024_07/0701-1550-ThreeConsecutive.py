# 3분소요. 51ms. 29.22% beats.

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for i in arr:
            if i % 2 == 1:
                cnt += 1
                if cnt >= 3:
                    return True
            else:
                cnt = 0
        return False