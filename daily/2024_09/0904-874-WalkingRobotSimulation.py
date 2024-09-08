# 8:13 시작. 1차시도. 메모리 초과.
# 2차시도. obst를 변경. 285ms. 58% beats.

# obst를 생각 못했다. 그냥 집합의 좌표 자체를 set으로 보고, 그거를 in 으로 찾아서 break를 걸어주면 되는 거였는데.
# dict의 key도 마찬가지일테고,

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        move = deque([(0,1),(1,0),(0,-1),(-1,0)])
        init = [0,0]
        obst = set(map(tuple,obstacles))

        # 장애물은 어떻게 구현할건데? 매번마다 장애물 루프 돌수도 없고,
        # 0,0일때, hashtable로 장애물 찍어놓고,
        # command 하나당, -1,-2를 제외하고, for문을 돌린다고 생각하면 된다.
        # 할때마다 장애물 있나? 이걸 고려하고,

        def calc_dist(x,y):
            return abs(x)**2 + abs(y)**2
        
        dist = 0

        for i in commands:
            if i == -1:
                move.append(move.popleft())
            elif i == -2:
                move.appendleft(move.pop())
            else:
                dx,dy = move[0]
                for _ in range(i):
                    nx, ny = init[0]+dx, init[1]+dy
                    if (nx,ny) in obst:
                        break
                    init[0] += dx
                    init[1] += dy
            dist = max(dist,calc_dist(init[0],init[1]))

        return dist