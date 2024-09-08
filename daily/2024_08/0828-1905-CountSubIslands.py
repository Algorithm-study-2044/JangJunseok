# 5:50 시작. 6:13. 시간 초과. 2154ms. 47.95% beats.

# 일단 섬을 어떻게 구하나?
# 생각한 방법은, 2에서 섬을 다 구한다음에, 
# 해당 섬의 시작점을 가지고 있다가,
# BFS를 돌린다. 그래서 다 0으로 지워주고
# 1 지점을 다 돈다. 그런데 해당 지점 0이 나왔따? 그럼 그건 섬이 아니닌까
# 플래그가 안섰따? 그러면 그거는 카운팅해준다.

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        cnt = 0

        def BFS(init_point):
            nonlocal cnt
            x,y = init_point
            queue = deque([(x,y)])
            dx = [0,0,1,-1]
            dy = [1,-1,0,0]
            flag = False

            while queue:
                x,y = queue.popleft()
                # 해당 지점을 지워준다.
                grid2[y][x] = 0

                if grid1[y][x] == 0:
                    # 이러면 그 지점은 있는데, grid1에는 없다는 거니까, sub-island 아님
                    flag = True
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if ny >= 0 and ny < len(grid2) and nx >= 0 and nx < len(grid2[ny]) and grid2[ny][nx] == 1:
                        # 근데 왜 여기서 안해주면 시간초과가 나는걸까? 
                        # a,b,c,d a1,b1,c1,d1

                        # 아. 왼쪽 아래랑 아래 왼쪽은 같은 거니까,
                        grid2[ny][nx] = 0
                        queue.append((nx,ny))
                
            if not flag:
                cnt += 1

        for y in range(len(grid2)):
            for x in range(len(grid2[y])):
                if grid2[y][x] == 1:
                    BFS((x,y))
            
        return cnt
        