# 1차시도. 틀렸다는데, 문제는 전체다. 전체가 작아야 한다는 것이다.
# 만약에 최소 비용이 꽃을 피웠는데, 그게 다른 최소비용을 가린다면, 그거는 최소가 안된다는 것이다.
# DFS로 다시 풀어보자.

import sys
import heapq

n = int(input())

res = []
my_heap = []
my_set = set()
total = 0
total_cnt = 0

def checkVisited(arr):
    isVisited = False

    for item in arr:
        if item in my_set:
            isVisited = True

    return isVisited


for i in range(n):
    arr = list(map(int,sys.stdin.readline().split()))
    res.append(arr)

for row in range(1,n-1):
    for col in range(1,n-1):
        cnt = 0
        cnt += res[row][col]
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        visited = [(row,col)]

        for i in range(4):
            newX = row+dx[i]
            newY = col+dy[i]
            cnt += res[newX][newY]
            visited.append((newX, newY))
            
        heapq.heappush(my_heap,(cnt,visited))

while total < 3:
    cnt, visited = heapq.heappop(my_heap)
    if checkVisited(visited):
        continue
    else:
        for item in visited:
            my_set.add(item)
        
        total += 1 
        total_cnt += cnt

print(total_cnt)



# 2차시도.

import sys

def check(i, j, visited):
    for idx in range(4):
        ni = i + d[idx][0]
        nj = j + d[idx][1]
        if (ni, nj)  in visited:
            return False
    return True

def dfs(visited, total):
    global answer
    if total >= answer:return
    if len(visited) == 15:
        answer = min(answer, total)
    else:
        for i in range(1, N-1):
            for j in range(1, N-1):
                if check(i, j, visited) and (i, j) not in visited:
                    temp = [(i, j)]
                    temp_cost = fields[i][j]
                    for idx in range(4):
                        ni = i + d[idx][0]
                        nj = j + d[idx][1]
                        temp.append((ni, nj))
                        temp_cost += fields[ni][nj]
                    dfs(visited + temp, total + temp_cost)

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N = int(input())
answer = int(1e9)
fields = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dfs([], 0)

print(answer)
