# 2분. pass
class Solution(object):
    def minimumOperations(self, nums):

        nums_1 = [item for item in nums if item != 0]    
        return len(set(nums_1))