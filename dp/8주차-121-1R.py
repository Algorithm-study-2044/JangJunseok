# 각 막대 입장에서, 그 막대 왼쪽에서,
# 그 막대와 가장 차이가 많이 날 것 같은 애는 누구에요? 그걸 계산한거다.
# 여기서는 dp를 굳이 array로 줄 필요가 없고.

# 이거는 중복된 계산을 한다기 보다는, 불필요한 계산을 없앤다는 것이다.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        maxVal = 0

        for i in range(1,len(prices)): 
            maxVal = max(prices[i] - start, maxVal)

            if prices[i] < start:
                start = prices[i]
        
        return maxVal