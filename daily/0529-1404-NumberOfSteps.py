# 1차시도. 36ms. 60% beats.

class Solution:
    def numSteps(self, s: str) -> int:
        
        res = int(s,2)

        def back_tracking(num,cnt):
            if num == 1:
                return cnt
            
            if num % 2 == 0:
                return back_tracking(num // 2, cnt + 1)
            else:
                return back_tracking(num + 1, cnt + 1)
        
        return back_tracking(res,0)
    
