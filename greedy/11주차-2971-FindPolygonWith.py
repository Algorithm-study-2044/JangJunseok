# 12분 소요. 517ms. 63.69% beats.

from collections import deque
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        dd = deque(nums)
        all = sum(dd)
        res = -1
        for i in range(len(dd)-1,-1,-1):
            if all > dd[i] * 2:
                res = sum(dd)
                break
            else:
                sub = dd.pop()
                all -= sub
        
        return res