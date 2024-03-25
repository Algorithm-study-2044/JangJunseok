# 1차시도 실패.

# 2 1 1 
# 1 1 1
# 0 1 2

# 이것의 정답이 왜 2지??
# 3 아니낙?

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