# 6주차. 20분 소요. 532ms. 94% beats.

class Solution(object):
    def findJudge(self, n, trust):

        if n == 1:
            return 1
        
        map = [0] * (n+1)

        for t in trust:
            map[t[1]] += 1
        
        arr = [idx for idx, val in enumerate(map) if val == n-1]

        for idx in arr:
            if all([item[0] != idx for item in trust]):
                return idx
        
        return -1
