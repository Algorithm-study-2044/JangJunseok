# 8:13 시작. 17분. 6386ms. 5% beats.

# 이거는 각 시작점마다 체크를 하는게 맞음.
# 0이 아니면 시작. 상하좌우로 1씩 이동한 좌표를 BFS에 넣고,
# 만약 그 지점이 0이나 grid를 벗어나는, 혹은 방문한 지점이었다. 그러면 ans랑 비교.

# 근데 copy를 안해주면 왜 안될까. 그게 좀 이해가 안됨.

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ans = [0]

        def DFS(x,y,seen,curr):
            if y < 0 or y >= len(grid) or x < 0 or x>=len(grid[y]) or (x,y) in seen or grid[y][x] == 0:
                ans[0] = max(ans[0],curr)
                return

            seen.add((x,y))
            curr += grid[y][x]
            
            DFS(x+1,y,seen.copy(),curr)
            DFS(x-1,y,seen.copy(),curr)
            DFS(x,y-1,seen.copy(),curr)
            DFS(x,y+1,seen.copy(),curr)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                DFS(j,i,set(),0)
        
        return ans[0]


# 다른 사람의 풀이. 3004ms.
# 나 같은경우에는 seen을 계속 복사해서 넘겼는데, 이 사람은 그냥 하나의 seen가지고 그걸 계속 복사해서 사용한 것.

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
