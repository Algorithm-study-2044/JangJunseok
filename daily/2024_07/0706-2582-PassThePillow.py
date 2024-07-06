# 10:14 시작. easy문제. 31ms. 77.47% beats.

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if (time // (n-1)) % 2 == 0:
            return 1 + (time % (n-1))
        
        return n - (time % (n-1))