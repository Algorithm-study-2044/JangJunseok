# 10:36 시작. 485ms. 93.41% beats.

# 줄일 수 있는 방법이 있나? 
# -3 입장에서 
# 왼쪽것의 최대.

# each one should choose.
# left maximum + curr versus curr
# which one is big? 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = nums[i] if dp[i-1] < 0 else dp[i-1] + nums[i]
        return max(dp)