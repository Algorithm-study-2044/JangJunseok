# 11:35 시작. 12:10분. 35분 소요. 그러나 정답이 이상하게 나오는데.
import sys
from itertools import permutations, combinations

# 그러니까 처음에 조합을 구한다음에,
# 그거의 permute를 해서, 구한다고 보면.


n = int(input())
arr = list(range(n))
grid = []

for i in range(n):
    grid.append(
        list(map(int,sys.stdin.readline().split())))
    
# print(grid)
minval = float("inf")

comb = list(combinations(arr,len(arr)//2))
comb2 = []

for item in comb:
    t2 = [x for x in arr if x not in item]
    ax = [item,t2]
    comb2.append(ax)

def calc_synerge(arr):
    dd = list(permutations(arr,2))
    res = 0
    for x,y in dd:
        res += grid[x][y]
        res += grid[y][x]

    return res


for first,second in comb2:
    fv = calc_synerge(first)
    sv = calc_synerge(second)
    minval = min(abs(fv-sv),minval)

print(minval)



# 2차시도. 다른 사람의 풀이 참고. 조합 활용.

import sys

from itertools import combinations

N = int(sys.stdin.readline())

stat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# zip(*stat)이 행렬을 전치한다. *stat이 행렬을 unpack하는거고.  
sum_stat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))] # 대각선끼리 합

# sum_stat에는 1부터 N까지의 선수에 있어, 각 선수가 낼 수 있는 시너지 합이 들어있다.
# 내가 궁금했던 건. 이런식으로 내 팀이 아닌 선수들과의 시너지까지 포함되었다고 했을때, 그것을 뺄 수 있는 방법이 있을까?에 대한 문제였음.

# 그냥 stat의 모든 원소 합으로 계산해도 됨.
allstat = sum(sum_stat) // 2 

result = float('inf')

# 즉 원리는, 각 선수가 낼 수 있는 시너지의 합을 sum_stat에 넣고, 그 중에서 N//2개를 봅아서, 그것의 합이 그 팀의 시너지 합.

for l in combinations(sum_stat, N//2): 
    result = min(result, abs(allstat - sum(l))) 


# 3차시도. 다른 사람의 풀이 참고. 백트래킹 활용.

def team(a,n):
    global result
    if a == N//2: # 유망하다면
        start, link = 0, 0 # start 팀, link팀
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]: # 만약 i, j 둘다 방문한거라면
                    start += S[i][j] # 스타트팀에 배정
                elif not visited[i] and not visited[j]: # i,j 둘다 방문 안했으면
                    link +=S[i][j] # 링크 팀에 배정
        result = min(result,abs(start-link)) # 최소값
        return
    else :
        for x in range(n,N): 
            if visited[x] == 0: # 방문 안했으면
                visited[x] = 1 # 방문 체크
                team(a+1,x+1) # 횟수 늘려
                visited[x] = 0 # 되돌아가
import sys
N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [0]*N
result = float('inf')
team(0,0)
print(result)