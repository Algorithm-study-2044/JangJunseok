# 1차시도. 17분. 116ms. 76% beats.

class Solution(object):
    def findContentChildren(self, g, s):
        g = sorted(g)
        s = sorted(s)
        cnt = 0
        qIndex = 0
        
        for greedy in g:
            while qIndex < len(s) and s[qIndex] < greedy:
                qIndex += 1
            if qIndex >= len(s):
                break
            
            # 쿠키를 받은 상황
            qIndex += 1
            cnt += 1
            
        return cnt