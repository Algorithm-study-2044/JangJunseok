# 7:50 시작. 35분소요. 1차시도. 메모리 초과. 아무래도 갔던곳을 다시 가서 그런것같기도 하고.

# [[1,1,1,1,1]]
# [[1,0,0,0,1]]
# [[1,0,1,0,1]]
# [[1,0,0,0,1]]
# [[1,1,1,1,1]]

# 그럼 bfs를 돌려서, 1을 k로 다 바꿔버린다.
# 그런 다음에, 이제 다시 돌려봐, 그런데도 1이 있다? 그러면 걔는 p.

# 그 다음에 p를 정해서, 걔를 bfs 다 돌린다. 만약 k를 만난다? 그르면 거기서 dist return
# 아니다. 그냥 섬 하나 정한다음에, 그 섬의 모든 점에서 (가능한한 외곽쪽만) bfs를 돌린다.
# 이때 얼마만큼 다리를 쌓았는지도 체크해야함.

class Solution(object):
    def shortestBridge(self, grid):
        # turn 1 to grid
        def DFS((x,y),grid,flag,save,visited):
            
            dx = [1,-1,0,0]
            dy = [0,0,1,-1]

            if grid[x][y] == 1:
                if not flag[0]:
                    grid[x][y] = "k"

                elif (x,y) not in visited:
                    grid[x][y] = "p"
                    visited.add((x,y))
                    save.append((x,y,0))

                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if nx >= 0 and nx <= len(grid)-1 and ny >=0 and ny <= len(grid[nx])-1:
                        DFS((nx,ny),grid,flag,save,visited)

        flag = [False]
        saveP = deque([])
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    DFS((i,j),grid,flag,saveP,visited)
                    flag[0] = True
        
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]


        while saveP:
            (i,j,dist) = saveP.popleft()
            # 4방향을 탐색해서, 그 중에 하나라도 k가 있따? 그러면 그 length를 return.
            # 그렇지 않다면, 이제는 0이 있따? 그러면 0을 다시 stack에 넣는다. 

            for t in range(4):
                nx = i + dx[t]
                ny = j + dy[t]
                if nx < 0 or nx > len(grid) -1 or ny < 0 or ny > len(grid[nx])-1:
                    continue
                if grid[nx][ny] == "k":
                    return dist
                elif grid[nx][ny] == 0:
                    saveP.append((nx,ny,dist+1))

    
# 2차시도. 첫번째 DFS를 BFS로 바꿔보았음. 마찬가지로 메모리 초과.

from collections import deque

class Solution(object):
    def shortestBridge(self, grid):
        def BFS(start, grid, flag, save, visited):
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            queue = deque([start])
            visited.add(start)

            while queue:
                x, y = queue.popleft()
                if grid[x][y] == 1:
                    if not flag[0]:
                        grid[x][y] = "k"
                    else:
                        grid[x][y] = "p"
                        save.append((x, y, 0))

                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited:
                            queue.append((nx, ny))
                            visited.add((nx, ny))

        flag = [False]
        saveP = deque([])
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    BFS((i, j), grid, flag, saveP, visited)
                    flag[0] = True

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        while saveP:
            (i, j, dist) = saveP.popleft()

            for t in range(4):
                nx = i + dx[t]
                ny = j + dy[t]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]):
                    if grid[nx][ny] == "k":
                        return dist
                    elif grid[nx][ny] == 0:
                        saveP.append((nx, ny, dist + 1))
