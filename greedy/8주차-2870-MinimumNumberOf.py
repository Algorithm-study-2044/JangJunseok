# 1차시도. 19분. 687ms. 15% beats.

class Solution(object):
    def minOperations(self, nums):
        cnt = Counter(nums)
        res = 0
        for item in cnt.values():
            if item == 1:
                return -1
            
            if item % 3 == 0:
                res += item // 3
            elif item % 3 == 1:
                res += (item // 3 + 1)
            elif item % 3 == 2:
                res += (item // 3 + 1)
        return res