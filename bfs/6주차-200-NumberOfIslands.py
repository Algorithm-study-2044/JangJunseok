#6주차. 1차시도. 시간초과. 23분 소요. BFS로 풀었으나 메모리 초과가 발생.  

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
                if x < 0 or y < 0 or x >= len(grid[curY]) or y >= len(grid) or grid[curY][curX] == "0":
                    continue
                
                grid[curY][curX] = 0

                for i in range(4):
                    newX = curX + dx[i]
                    newY = curY + dy[i]
                    queue.append((newX,newY))

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    cnt += 1
                    BFS(x,y)
        
        return cnt


#2차시도. DFS로 풀이.
    
from collections import deque

class Solution(object):    
    def numIslands(self, grid):
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        cnt = 0

        def DFS(x,y):
            if y <0 or x < 0 or y >= len(grid) or x >= len(grid[y]) or grid[y][x] != "1":
                return

            grid[y][x] = "0"

            for i in range(4):
                newX = x + dx[i]
                newY = y + dy[i] 
                DFS(newX,newY)
        
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == "1":
                    cnt += 1
                    DFS(x,y)
        
        return cnt