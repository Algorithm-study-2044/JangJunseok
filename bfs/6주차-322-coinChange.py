#6주차. 1차시도. 10분 소요. 746ms. 67% beats. dp로 풀었음. 279번이랑 비슷함.

class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1,amount+1):
            min_value = float('inf')
            for c in coins:
                if i-c < 0:
                    continue
                min_value = min(min_value, dp[i-c]+1)
            dp[i] = min_value
        
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]