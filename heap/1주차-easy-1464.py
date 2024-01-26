#3분 소요. pass.
class Solution(object):
    def maxProduct(self, nums):
        nums.sort(reverse=True)
        return (nums[0]-1) * (nums[1]-1)
        