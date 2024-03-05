#6주차. 1차시도. 시간초과. 23분 소요. BFS로 풀었으나 시간초과가 발생했다.   

from collections import deque

class Solution(object):
    def numIslands(self, grid):
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        cnt = 0
        
        def BFS(x,y):
            queue = deque([(x,y)])

            while queue:
                curX, curY = queue.popleft()
                grid[curY][curX] = 0

                for i in range(4):
                    newX = curX + dx[i]
                    newY = curY + dy[i]
                    if newY < 0 or newY >= len(grid) or newX < 0 or newX >= len(grid[newY]):
                        continue
                    if grid[newY][newX] == "1":
                        queue.append((newX,newY))

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    cnt += 1
                    BFS(x,y)
        
        return cnt