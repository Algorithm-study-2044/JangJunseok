#4주차. 98ms. 77% beats.

class Solution(object):
    def merge(self, intervals):
        
        arr = sorted(intervals, key=lambda x:x[0])
        res = []
        curr = [-1,-1]

        for item in arr:
            if curr[1] < item[0]:
                res.append(curr)
                curr = item
            else:
                curr[1] = max(curr[1],item[1])

        res.append(curr)
        res.pop(0)
        return res