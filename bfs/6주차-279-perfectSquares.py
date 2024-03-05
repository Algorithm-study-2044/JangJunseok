
# 2차시도. 다른 사람의 풀이 연구.
class Solution(object):
    def numSquares(self, n):
        
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(1,n+1):
            j = 1
            min_val = float('inf')
            while j*j <= i:
                min_val = min(min_val, dp[i-j*j] + 1)
                j += 1
            dp[i] = min_val
        
        return dp[n]
                # 무조건 큰수부터 하면 되는거 아닌가? 할 수 있지만.
                # 그 수에 해당하는 path가 없으면, 무한대가 되어버리니까.
                # 항상 최소가 dp[i-j*j] + 1이라고는 할 수 없다.

        #dp[i]를 구해야 함.


#1차시도. 메모리초과. 중간에 curr를 num으로 잘못썼고, i**2를 안해서 디버깅하느라 시간을 많이 씀.

from collections import deque
import math

class Solution(object):
    def numSquares(self, n):
        
        def getSqaureArr(num):
            res = []
            
            for i in range(1,int(math.floor(math.sqrt(num)))+1):
                res.append(i**2)

            return res

        def BFS(num,depth):
            queue = deque([(num,depth)])

            while queue:
                curr, depth = queue.popleft()
                if curr == 0:
                    return depth
                else:
                    arr = getSqaureArr(curr)
                    for item in arr:
                        queue.append((curr-item, depth+1))
        
        return BFS(n,0)
    

