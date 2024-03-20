# 3:53분. 1차시도 실패. 30분 소요.

class Solution(object):
    def maxSubArray(self, nums):
        dp = [[0] * (len(nums)+1)] * len(nums)
        
        start = 0
        end = 0        
        while start <= len(nums):       
            
            if end >= len(nums):
                start += 1
                end = start
                continue
            
            if nums[end] < 0:
                dp[start][end+1] = dp[start][end] + nums[end]
                end += 1

            elif nums[end] > 0:
                dp[start][end+1] = dp[start][end] + nums[end]
                end += 1

        print(dp)
        return max([max(myList) for myList in dp])


