#1차시도. 성공. 1081ms. 5% beats.

class Solution(object):
    def maxSubArray(self, nums):
        rdp = [0] * (len(nums))
        for i in range(len(nums)-2,-1,-1):
            rdp[i] = max(0,max(rdp[i+1]+nums[i+1],nums[i+1]))

        ldp = [0] * (len(nums))
        for i in range(1,len(nums)):
            ldp[i] = max(0,max(ldp[i-1]+nums[i-1],nums[i-1]))
            
        res = max(nums)
        for i in range(len(nums)):
            res = max(res,ldp[i]+rdp[i]+nums[i])
        
        return res