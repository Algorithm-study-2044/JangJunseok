# 1:41 시작. 7분 소요. 73ms. 17.88% beats
# 전에 나왔던거랑 거의 유사한 문제.

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        arr = [0] * len(s)
        for i in range(len(s)):
            arr[i] = abs(ord(t[i]) - ord(s[i]))
        
        start = 0
        end = 1
        res = 0
        curr = arr[0]
        while start <= end and end <= len(arr):
            if curr <= maxCost:
                res = max(res,end-start)
                if end < len(arr):
                    curr += arr[end]
                end += 1
            else:
                curr -= arr[start]
                start += 1
            
        return res