#1차시도. 20분. 시간초과 실패. 

class Solution(object):
    def maxProfit(self, prices):
        
        start = 0
        end = 1
        maxOf = [0] * (len(prices) - 1)
        maxVal = 0

        while start < len(prices) - 1:
            if end == len(prices):
                maxVal = max(maxVal, maxOf[start] - prices[start])
                start += 1
                end = start + 1
                continue

            if prices[end] > maxOf[start] and prices[end] - prices[start] > 0:
                maxOf[start] = prices[end]

            end += 1
        
        return maxVal
    
# 2차시도. 시간초과 실패.

class Solution(object):
    def maxProfit(self, prices):
        
        start = 0
        maxVal = 0

        while start < len(prices) - 1:
            maxVal = max(max(prices[start+1:])-prices[start], maxVal)
            start += 1
        
        return maxVal
    

# 3차시도. 다른사람의 풀이 연구.

# 이게 왜 되는거지? 
# 이 아이디어는. 만약에 오른쪽 요소가 왼쪽보다 작다면. 더 작다는 거니까 그걸 매수하면 되는 것이다.
# 그래서 left = right로 옮겨주는 것이다.

class Solution:
    def maxProfit(self,prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit


#이 solution도 비슷하다. 오른쪽으로 계속 가는데, 만약에 왼쪽보다 작은게 나오면, 
#굳이 이제는 왼쪽거를 그대로 두면서 비교할 필요가 없는거다. 왼쪽을 오른쪽으로 옮겨주면 되는거다.

class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit