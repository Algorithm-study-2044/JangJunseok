# 2:54. 15분 소요. 653ms. 27.07% beats.
# heap을 사용해서 풀었음.

# 생각한 과정.

# 그러니까 언제 안되는건가 하면.
# 한마리이면 거리가 1, speed 1 초과이면 안됨.
# False, 1, 2, 3 
# 여기서 일단 다음발 장전되었다고 가정하려면 speed를 빼주면 된다.
# 이때 이미 dist가 0보다 작거나 같으면 out이 되는거고.
# dist / speed해서 가장 작게 나오는 넘부터.
# heap = [1,1,2,3] 이렇게 될거고
# 하나 빼준다음에, cnt += 1 해주고 [1,2,3] 에서 다음거 꺼낸다음에 cnt만큼 빼준다.
# 그랬을때 그게 0 미만이다? 글면 그때까지의 cnt를 반환하면 되는거고
# 만약 다 죽였다? 그러면 while문 빠져나와서, cnt를 반환하면 되는거고.

import heapq

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        hp = []
        # 각각의 몬스터가 몇초에 도착하는지 계산해서 heap에 넣어준다.
        for i in range(len(dist)):
            heapq.heappush(hp,dist[i] / speed[i])
        cnt = 0
        while hp:
            curr = heapq.heappop(hp)
            # 걸린시간보다 해당 몬스터의 도착 시간이 더 빠르다면, 게임 오버이다.
            if curr - cnt <= 0:
                return cnt
            # 잡은 몬스터수만큼 시간이 걸릴거다.
            cnt += 1
        
        return cnt