#2주차. 3분소요. pass. 136ms. 61% beats.

class Solution(object):
    def maximizeSum(self, nums, k):
        result = 0
        result += max(nums) * (k)
        for i in range(1,k):
            result += i
        return result
