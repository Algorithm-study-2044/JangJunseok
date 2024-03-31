#6:45분. 1차시도. 실패. 27분 소요.

class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        req = []
        # 가장 편차가 심한 부분은 ladder를 쓰고,
        # 그게 아니면 bricks를
        
        # 근데 문제는, 가장 길다고 해서 bricks를 썼는데, 
        # 그 전까지 bricks를 써서 못가면 안된다는 것이다.
        
        # 필요한 벽돌 개수와 넘어갈 index
        # (5,2) (3,4) (6,5) 이렇게 있을때,
        # bricks 5 ladders 1이라고 한다면,
        
        # ladders는 아예 여기서 삭제를 하는거고
        # heappop() 해서 가장 큰 것 두개를 pop했을때,
        # 나오는 max index를 가지고 있고,

        for i in range(1,len(heights)):
            need = heights[i] - heights[i-1]
            if need > 0:
                req.append([need,i])


# 2차시도. 다른 사람의 풀이 참고. 힙이 있으면,
# 일단 집어넣고 나중에 바꾸는 풀이도 가능하다.

                
import heapq

class Solution:
    def furthestBuilding(self, h: List[int], b: int, l: int) -> int:
        p = []
        
        for i in range(1,len(h)):
            diff = h[i] - h[i-1]
        
            if diff <= 0:
                continue
        
            # bricks로 커버되면 일단 그걸로 땜빵친다.
            b -= diff
            heapq.heappush(p,-diff)
            
            if b <0:
                if l <= 0:
                    # 더 이상은 못간다.
                    return i-1
                else:
                    curr = heapq.heappop(p)
                    b += -curr
                    l -= 1
        
        return len(h) - 1

                


        

  

    