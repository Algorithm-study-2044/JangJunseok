# 2차시도. 다른 사람의 풀이. 110ms. 94.27% beats.

from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        o = "O"
        
        n = len(board) 
        m = len(board[0])

        Q = deque()
        
        # 엣지이면서 o인 지점들을 찾아서 q에 넣는다.
        for i in range(n):
            if board[i][0] == o:
                Q.append((i,0))
            if board[i][m-1] == o:
                Q.append((i, m-1))
                
        for j in range(m):
            if board[0][j] == o:
                Q.append((0,j))
            if board[n-1][j] == o:
                Q.append((n-1, j))
                
        def inBounds(i,j):
            return (0 <= i < n) and (0 <= j < m)
                
        while Q:
            i,j = Q.popleft()
            board[i][j] = "#"
            
            for ii, jj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if not inBounds(ii, jj):
                    continue
                if board[ii][jj] != o:
                    continue
                    
                # 이제 해당 엣지지점과 연결된 o를 찾아서 다 #로 바꿔준다.
                Q.append((ii,jj))
                board[ii][jj] = '#'
            
        for i in range(n):
            for j in range(m):
                if board[i][j] == o:
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = o

# 1차시도. 시간초과.
# 내 풀이는, 한번의 BFS에서, 일단 o를 찾고, edge가 아닌지를 확인한다음 한번 더 iterate를 도는 식이었다.
# 다른 사람의 풀이는, edge에 있는 o를 찾고, 즉 mn + mn = 2mn만큼의 시간복잡도로 edge에 있는 o는 임시로 #로 바꿔준다음에 나중에 o로, 그 다음에 그래도 o인놈들은 X로 바꿔주는 방식이다.
# 내 풀이는, 일단 o를 찾고, edge가 아닌지를 확인하고, 

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def check_is_on_edge(point,board):
            x,y = point
            if y <= 0 or y >= len(board) -1 or x <= 0 or x >= len(board[y]) -1:
                return True
            return False

        seen = set()

        def BFS(point,board):
            queue = deque([point])
            seen.add(point)
            dx = [0,0,1,-1]
            dy = [1,-1,0,0]

            while queue:
                curr = queue.popleft()
                seen.add(curr)
                
                for i in range(4):
                    px = dx[i] + curr[0]
                    py = dy[i] + curr[1]

                    if check_is_on_edge([px,py],board) and board[py][px] == "O":
                        return

                    if board[py][px] == "O" and (px,py) not in seen:
                        queue.append((px,py))
        
            for x,y in seen:
                board[y][x] = 'X'                    

        for y in range(len(board)):
            for x in range(len(board[y])):
                if not check_is_on_edge((x,y),board) and board[y][x] == "O" and (x,y) not in seen:
                    BFS((x,y),board)