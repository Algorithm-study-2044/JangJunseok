# 11:42 시작. 6091ms. 5% beats.

# 어디서 틀린지 알겠다. 각 루트에서 돌아가면 안되지만,
# 각 루트와 다른 루트는 구분되어야 한다.

# 그를 위해서 각 루트마다의 set을 새롭게 생성했는데, 

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        res = [0]
        step_x = [0,0,1,-1]
        step_y = [1,-1,0,0]

        def BFS(item):
            queue = deque([(item[0], item[1], 0, set())])
            flag = False

            while queue:
                x, y, point, seen = queue.popleft()
                point += grid[y][x]
                new_seen = seen.copy()
                new_seen.add((x,y))
                res[0] = max(res[0],point)

                for i in range(4):
                    next_x = x + step_x[i]
                    next_y = y + step_y[i]

                    if next_y >= 0 and next_y < len(grid) and next_x >=0 and next_x < len(grid[next_y]) and grid[next_y][next_x] != 0 and (next_x,next_y) not in new_seen:
                        queue.append((next_x,next_y,point,new_seen))

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] != 0:
                    BFS((col,row))
        
        return res[0]
        

# 다른 사람의 풀이.
# 재귀를 해서, 각 지점마다의 최대값을 구한다.
# 그걸 다시 이전의 최대값으로 보내고, 그런식으로.

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = [[0] * col for _ in range(row)]
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 0:
                    ans = max(self.find_max(grid, visited, i, j), ans)
        return ans
    
    def find_max(self, arr, visited, i, j):
        if (i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]) or
                visited[i][j] == 1 or arr[i][j] == 0):
            return -1000000
        
        visited[i][j] = 1
        a = self.find_max(arr, visited, i + 1, j)
        if a < 0:
            a = 0
        b = self.find_max(arr, visited, i - 1, j)
        if b < 0:
            b = 0
        c = self.find_max(arr, visited, i, j + 1)
        if c < 0:
            c = 0
        d = self.find_max(arr, visited, i, j - 1)
        if d < 0:
            d = 0
        visited[i][j] = 0
        return max(max(a, b), max(c, d)) + arr[i][j]
