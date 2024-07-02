#129ms. 34% beats.

class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        candies = [1] * N
        for i in range(N):
            if i == 0:
                continue
            
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        for i in range(N-1,-1,-1):
            if i == N-1:
                continue
            
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1
                
        return sum(candies)
    

class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        down = 0
        up = 0
        res = N
        prevSame = False

        if ratings[1] < ratings[0]:
            res += 1

        for i in range(len(ratings)):
            if i == 0:
                continue

            if ratings[i] > ratings[i-1]:
                down = 0
                up += 1
                res += up
                prevSame = False

            elif ratings[i] < ratings[i-1]:
                down += 1
                res += (down-1)
                if prevSame:
                    res += 1
                # 왜? 그 다음거는 1이 되니까. 그런데,
                # 이때 그 이전꺼가 사탕 1개인 경우에는, down을 더 먹여줘야 한다.
                # 그 이전꺼가 사탕 1개가 되는 경우는, 5 -> 5 -> 3 이렇게, 같아져서 1이 되었다가 내려가는 경우.
            else:
                up = 0
                down = 0
                prevSame = True
                # 두 ratings가 같다? 그러면 같이 해줄 필요가 없다.
        
        return res