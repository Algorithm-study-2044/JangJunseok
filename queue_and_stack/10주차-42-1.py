#11:30분 시작. 11:45분까지. 131ms. 5% beats.
import heapq

class Solution(object):
    def trap(self, height):
        l = [0] * len(height)
        maxl = [(0,0)]
        
        for i in range(len(height)):
            l[i] = maxl[0][1]
            heapq.heappush(maxl,(-height[i],height[i]))

        r = [0] * len(height)
        maxr = [(0,0)]
        
        for i in range(len(height)-1,-1,-1):
            r[i] = maxr[0][1]
            heapq.heappush(maxr,(-height[i],height[i]))

        res = 0
        for i in range(len(height)):
            res += max(min(l[i],r[i])-height[i],0)

        return res
    

# 다른 사람의 풀이.

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        left = [0] * n
        right = [0] * n
        
        # Fill left array
        left[0] = height[0]
        for i in range(1, n):
            # 아니다. 지금 이거는 height[i-1]이 아니라, left[i-1]이다.
            # 그러므로 left[i]에는, 지금까지 중에서 가장 큰 것이 살아남을 것이다.
            # 나는 heap을 썼는데, 사실 최대값 구하는거같으면 그냥 이렇게 iterate해도 되는것이다.
            left[i] = max(left[i - 1], height[i])
        
        # Fill right array
        right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])        

        trappedWater = 0
        for i in range(n):
            # left[i] right[i] 가 둘다 height[i]보다 커야 성립 가능하다.
            trappedWater += min(left[i], right[i]) - height[i]
        
        return trappedWater               