#1차시도. 시간초과 실패.
class Solution(object):
    def longestIncreasingPath(self, matrix):
        
        maxLength = [0]

        def DFS(x, y, before, depth):
            #x,y에서, 4방향에다가 
            #만약에 before보다 큰 number가 아니면, return해준다.
            if y<0 or y>len(matrix)-1 or x<0 or x>len(matrix[y])-1 or matrix[y][x] <= before:
                maxLength[0] = max(depth,maxLength[0])
                return

            before = matrix[y][x]
            dx = [0,0,-1,1]
            dy = [1,-1,0,0]

            for i in range(4):
                DFS(x+dx[i],y+dy[i],before,depth+1)

        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                DFS(x,y,-1,0)

        return maxLength[0]
    

# 2차시도. 15ms. 

class Solution(object):
    def longestIncreasingPath(self, matrix):
        
        # 똑같은 matrix를 만들어준다.
        dp = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        def DFS(x, y, before, depth):
            if dp[y][x] != -1:
                #이미 그 부분이 계산이 되어있으면, 그 값을 주면 된다.
                return dp[y][x]
            else:
                #계산이 안되어있다면, 그 점에서의 최대 길이를 구한다음 return 하면 된다.
                #최대길이는? 사방향으로 뻗어가서, 그 점에서 또 DFS를 한 값이다.
                dp[y][x] = 1
                before = matrix[y][x]
                dx = [0,0,-1,1]
                dy = [1,-1,0,0]

                for i in range(4):
                    newX = x+dx[i]
                    newY = y+dy[i]
                    if newY<0 or newY>len(matrix)-1 or newX<0 or newX>len(matrix[newY])-1 or matrix[newY][newX] <= before:
                        continue
                    dp[y][x] = max(DFS(x+dx[i],y+dy[i],before,depth+1)+1,dp[y][x])
                
                return dp[y][x]

        c = 0
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                c = max(c,DFS(x,y,-1,1))

        return c