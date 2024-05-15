# 1차시도. 다른 사람의 풀이 참조. 25-54분.

class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)

        while left < right:
            mid = (left+right) // 2
            if self.canEatAll(piles,mid,h):
                # 먹을 수 있어? 그러면 더 줄이자.
                right = mid
            else:
                # 시간내에 못먹으면 더 먹어야 함. 
                left = mid+1
        
        return left
    
    def canEatAll(self,piles,speed,h):
        time = 0
        for i in piles:

            # 여기서 i // speed + 1 하면 틀림.
            # (i-1) // speed + 1 이어야 함.
            # 왜? speed와 동일할때는, 1이 나와야 하기 때문.

            time += i // speed + 1
            if time > h:
                return False
        return True
            


class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        # 최소 1개. 최대 max로 세팅해놓고,
        # 가장 작은거를 찾아가면 된다.
        # 원래 binary search할때는 mid > target 이런식으로 했었다.
        # 그래서 target이 어디에 있는지 찾아가는 방식이엇는데,

        # 여기서는 target이 없다. 그냥 조건에 맞는 최소값을 찾아가는 것이다.

        while left < right:
            mid = (left + right) / 2
            if self.canEatAll(piles, mid, h):
                right = mid
            else:
                left = mid + 1
        
        return left
    
    # 3 6 7 11 이고, speed가 4라고 하면,
    # 3/4 + 6/4 + 7/4 + 11/4 = 3 + 2 + 2 + 3 = 10

    # 아니 그냥 (pile/speed) + 1 하면 안되나?
    # 
    
    def canEatAll(self, piles, speed, h):
        time = 0
        for pile in piles:
            time += ((pile - 1) / speed) + 1
            if time > h:
                return False
        return True