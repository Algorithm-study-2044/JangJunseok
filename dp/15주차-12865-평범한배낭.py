#1차시도. 시간 초과. 시간복잡도는 얼마인가?
#문제의 조건을 잘 파악하는것도 중요. 아이템 중복으로 넣는게 안되잖아.

from collections import deque

N,K = map(int,input().split())

items = []
for _ in range(N):
    items.append(list(map(int,input().split())))

dp = [0] * (K+1)

queue = deque([0])
maxVal = -1

while queue:
    curr = queue.popleft()
    
    for weight,val in items:
        if curr + weight <= K:
            dp[curr+weight] = max(dp[curr+weight],dp[curr] + val)
            maxVal = max(maxVal, dp[curr+weight])
            queue.append(curr+weight)

print(maxVal)



# 2차시도. 

N, K = map(int, input().split())

items = []
for _ in range(N):
    items.append(list(map(int, input().split())))

dp = [0] * (K + 1)

for weight, value in items:
    for w in range(K,weight-1,-1):
        dp[w] = max(dp[w], dp[w-weight] + value)
        # K-weight+weight 까지하면 dp[weight]에서 dp[K]까지를 업데이트.

print(dp[K])

# 위에거랑 아래거랑 어떻게 다른건데.
# 아래 코드는, dp계산을 아래에서부터 하니까, 같은 것을 두번 계산해버릴 위험이 존재한다.
# 위에 코드는 다른가? dp[i+1]은 dp[i]에 대해서, 이전 값을 참조를 하니까, 그 다음 값으로는 사용 못하는거다.

for weight, value in items:
    for w in range(0,K-weight+1):
        dp[w+weight] = max(dp[w+weight],dp[w]+value)





# 다른 사람의 풀이.

import sys

N, K = map(int, input().split())
stuff = [[0,0]]

# 이렇게 하면 N+1개의 배열 안에 K+1개의 원소가 있는거고. 왜?
# 1~N+1까지 인덱스를 두고 싶으니까.
# 0개. 즉 하나도 고려 안한것도 넣어줘야 함.

knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))

# 냅색 문제 풀이
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0] 
        value = stuff[i][1]
       
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j] 
        # j >= weight이다. 즉, 넣을 수 있다. 
        # i는 고려다. i-1[j]를 ij에 대입한다면, 그거는 i번째 요소를 안넣고 j를 만드는게 최대라는 말이 되고.
        
        # 비교를 해보자는 것이다. 

        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

# knapsack. 즉 N의 요소를 고려하고 K만큼 공간이 있을때의 최대.
print(knapsack[N][K])