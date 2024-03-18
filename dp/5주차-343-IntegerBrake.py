#1주차. 15ms. 54% beats.

class Solution(object):
    def integerBreak(self, n):
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 1

        for k in range(3,n+1):
            for i in range(1,k//2+1):
                dp[k] = max(max(dp[i],i) * max(dp[k-i],k-i),dp[k])

        return dp[n]