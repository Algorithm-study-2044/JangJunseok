# 1:17 -> 5분 소요. 52ms. 49.05% beats.

class Solution:
    def largestOddNumber(self, num: str) -> str:
        res = -2
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2 == 1:
                res = i
                break
        
        if res == -2:
            return ""
        else:
            return num[0:res+1] 