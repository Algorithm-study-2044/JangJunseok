#1차시도. 시간초과 실패.

class Solution(object):
    def sumSubarrayMins(self, arr):
        #i는 길이, j는 시작점
        res = 0
        for i in range(1,len(arr)+1):
            for j in range(0,len(arr)+1-i):
                res += min(arr[j:j+i])
        
        return res % (10**9 + 7)