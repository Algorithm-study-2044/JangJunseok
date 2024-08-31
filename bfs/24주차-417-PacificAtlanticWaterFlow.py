# 2차시도. dp+bfs, 1201ms. 7.15% beats.

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        can_go = [[[False,False] for _ in range(len(heights[0]))] for _ in range(len(heights))]
        def BFS(init):
            x,y = init
            gone = [False, False] # pacific / atlantic
            queue = deque([(x,y)])
            visited = set()
            while queue:
                curr_x, curr_y = queue.popleft()
                visited.add((curr_x,curr_y))
                curr_heights = heights[curr_y][curr_x]
                
                dx = [0,0,1,-1]
                dy = [1,-1,0,0]

                for i in range(4):
                    next_x = curr_x + dx[i]
                    next_y = curr_y + dy[i]
                    no_go = False

                    if next_x <= -1 or next_y <= -1:
                        gone[0] = True
                        no_go = True

                    if next_y >= len(heights) or next_x >= len(heights[0]):
                        gone[1] = True
                        no_go = True

                    if gone[0] and gone[1]:
                        ans.append([init[1],init[0]])
                        can_go[y][x] = [True, True]
                        queue = []
                        break

                    if no_go or heights[next_y][next_x] > curr_heights or (next_x,next_y) in visited:
                        continue

                    # 다음 지점을 봤더니 되는 놈이네? 그러면 다음 지점 안가고 패스.
                    if (can_go[next_y][next_x][0] and can_go[next_y][next_x][1]):
                        ans.append([init[1],init[0]])
                        can_go[y][x] = [True, True]
                        queue = []
                        break

                    queue.append((next_x,next_y))
            
        for y in range(len(heights)):
            for x in range(len(heights[y])):
                BFS([x,y])

        return ans

# 1차시도 실패. 왜? 
# 내가볼때는 dp를 써야 한다. 만약에 어떤 점에서 다른 점으로 갔을때 그 지점에서 이미 계산되어 있다면,
# 거기서 굳이 BFS를 쓸 필요가 없으니까.

# pacific: x가 -1이하거나, y가 0미만
# atlantic: x가 len(heights[y])이상이거나, y가 len(heights)이상
# 이면 dot의 값을 업데이트 하고,

# 하나의 점은, dot = (pac,atlan) = (False,False) 이렇게 되어있어야 하고,
# 하나의 점이 True, True가 된다면, 그거는 되는거니까 global += 1 해주면 되고,


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        def BFS(init):
            x,y = init
            gone = [False, False] # pacific / atlantic
            queue = deque([(x,y)])
            visited = set()
            while queue:
                curr_x, curr_y = queue.popleft()
                visited.add((curr_x,curr_y))
                curr_heights = heights[curr_y][curr_x]
                
                dx = [0,0,1,-1]
                dy = [1,-1,0,0]

                for i in range(4):
                    next_x = curr_x + dx[i]
                    next_y = curr_y + dy[i]
                    no_go = False

                    if next_x <= -1 or next_y <= -1:
                        gone[0] = True
                        no_go = True

                    if next_y >= len(heights) or next_x >= len(heights[0]):
                        gone[1] = True
                        no_go = True

                    if gone[0] and gone[1]:
                        ans.append([init[1],init[0]])
                        queue = []
                        break

                    if no_go:
                        continue

                    if heights[next_y][next_x] <= curr_heights and (next_x,next_y) not in visited:
                        queue.append((next_x,next_y))
            
        for y in range(len(heights)):
            for x in range(len(heights[y])):
                BFS([x,y])

        return ans



