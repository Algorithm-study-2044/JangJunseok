# 1차시도 실패. 내가 착각한것. 하나만 골라서 시작하는게 아니라,
# 모든 rotten orange를 시작으로 해야한다.

from collections import deque,defaultdict

class Solution(object):
    def orangesRotting(self, grid):
        # BFS를 돌면서, 만약에 썩은 애가 하나라도 있으면, 
        # minute를 +1 해준다.
        
        minute = [0]

        def BFS((x,y)):
            queue = deque([(x,y,0)])

            step_x=[0,0,1,-1]
            step_y=[1,-1,0,0]
            depth_dict = defaultdict(lambda: False)

            while queue:

                currX,currY,depth = queue.popleft()
                curr_val = grid[currY][currX]

                if curr_val != 1:
                    continue
                
                grid[currY][currX] = 2

                if depth != 0 and not depth_dict[depth]:
                    depth_dict[depth] = True
                    minute[0] += 1
                    print("add minute on",(x,y),(currX,currY))
                for i in range(4):
                    nextX = currX+step_x[i]
                    nextY = currY+step_y[i]
                    if nextY < 0 or nextY >= len(grid) or nextX < 0 or nextX >= len(grid[nextY]):
                        pass
                    else:
                        next_val = grid[nextY][nextX]
                        if next_val == 1:
                            queue.append((nextX,nextY,depth+1)) 

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    grid[i][j] = 1
                    BFS((j,i))
        
        impossible = False
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    impossible = True    
        

        if impossible:
            return -1
        else:
            return minute[0]
        

# 2차시도. 다른 사람의 풀이 연구.        

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        #m은 행의 개수, n은 열의 개수.
        dr, dc = [1, -1, 0, 0], [0, 0, -1, 1]

        queue = collections.deque()
        fresh = []
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh.append((r, c))

        time = 0

        # 새롭게 썩은 애들만 queue에 넣어주면 된다.
        # 처음에 들어온 애들을 새롭게 썩은 애들로 생각하고,
        # 그 다음에 들어온 애들을 새롭게 썩은 애들로 생각하면 된다.

        # 만약에 처음에 썩은 애들이 다른 애들한테 옮겼는데, 그 애들이 다른 썩힐 애들이 없다면
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for i in range(4):
                    nr, nc = r+dr[i], c+dc[i]
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
            time += 1

        for r, c in fresh:
            if grid[r][c] == 1:
                return -1
                
        return time-1 if time else 0