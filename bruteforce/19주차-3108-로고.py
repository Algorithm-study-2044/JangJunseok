#2차시도. ======================================================================================
# 첫번째 문제의 경우 길이를 더블을 해주면 되는거엿음. 하지만 다시생각해볼것.

i = int(input())

minX = float("inf")
maxX = float("-inf")
minY = float("inf")
maxY = float("-inf")
start_point = []
ans = 0

for _ in range(i):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
    minX = min(minX, x1)
    maxX = max(maxX, x2)
    minY = min(minY, y1)
    maxY = max(maxY, y2)
    start_point.append((x1, y1, x2, y2))

arr = [[0] * (maxY - minY + 1) for _ in range(maxX - minX + 1)]

dx = -minX
dy = -minY

for x1, y1, x2, y2 in start_point:
    for x in range(x1, x2 + 1):
        arr[x + dx][y1 + dy] = 1
        arr[x + dx][y2 + dy] = 1
    for y in range(y1, y2 + 1):
        arr[x1 + dx][y + dy] = 1
        arr[x2 + dx][y + dy] = 1

def BFS(x, y):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if arr[cx][cy] == 1:
            arr[cx][cy] = 0
            for nx, ny in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
                if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] == 1:
                    stack.append((nx, ny))

for x1, y1, x2, y2 in start_point:
    if arr[x1+dx][y1+dy] == 1:
        print(x1,y1)
        ans += 1
        BFS(x1+dx,y1+dy)

#그엇을때 0,0이 0이라면 이거는 -1해주어야 함.

if arr[dx][dy] == 0:
    ans -= 1

print(ans)

# 1차시도 실패. 왜? 1로 표시된 부분을 탐색할 때, 한칸 띄워진 부분도 탐색해버림.
# 문제에서는 한칸 띄워진거는 다른 섬으로 보라고 했는데. 
# 그런데 그걸 어떻게 하지?

i = int(input())

minX = float("inf")
maxX = float("-inf")
minY = float("inf")
maxY = float("-inf")
start_point = []
ans = 0

for _ in range(i):
    x1, y1, x2, y2 = map(int, input().split())
    minX = min(minX, x1)
    maxX = max(maxX, x2)
    minY = min(minY, y1)
    maxY = max(maxY, y2)
    start_point.append((x1, y1, x2, y2))

arr = [[0] * (maxY - minY + 1) for _ in range(maxX - minX + 1)]

dx = -minX
dy = -minY

for x1, y1, x2, y2 in start_point:
    for x in range(x1, x2 + 1):
        arr[x + dx][y1 + dy] = 1
        arr[x + dx][y2 + dy] = 1
    for y in range(y1, y2 + 1):
        arr[x1 + dx][y + dy] = 1
        arr[x2 + dx][y + dy] = 1

def BFS(x, y):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if arr[cx][cy] == 1:
            arr[cx][cy] = 0
            # 이렇게 하면, 한칸 띄워진 부분도 그냥 탐색해버리는 문제가 있음.
            for nx, ny in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
                if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] == 1:
                    stack.append((nx, ny))

arr[dx][dy] = 1

for x1, y1, x2, y2 in start_point:
    print(x1,y1,x2,y2,arr[x1+dx][y1+dy])
    if arr[x1+dx][y1+dy] == 1:
        ans += 1
        BFS(x1+dx,y1+dy)

if arr[dx][dy] == 1:
    ans += 1

print(ans)


#다른 사람의 풀이 ======================================================================================

# 3108번 로고
# 자료 구조, 기하학, 분리 집합, 많은 조건 분기
'''
접근 방법:

PU명령은 펜을 떼라는 명령이다.

만약 두 직사각형이 서로 교차하는 점이 있다면,
우리는 그 두 직사각형을 펜을 떼지 않고 그릴 수 있음.
만약 두 직사각형이 만나지 않는다면, 무조건 펜을 한번은 떼야만 그릴 수 있다.

직사각형끼리 만나서 붙어있는 거를 "그룹"이라고 정의하자.
우리는 "그룹"을 펜을 떼지 않고 그릴 수 있다.(PU명령이 필요 없음)

따라서 PU명령의 최솟값을 구하라는 뜻은,
분리 집합을 이용하여 직사각형 "그룹"의 개수가 몇개인지 구하라는 뜻과 거의 같다.

이때, 문제에서 주어지기를 같은 선을 여러 번 그릴 수 있지만,
직사각형 N개를 제외한 어떤 것도 그릴 수 없다고 했고,
제일 처음의 거북이의 위치는 (0,0)에 위치해 있다고 했으므로,

그룹의 개수를 다 구한 뒤에 만약 직사각형들 중에서 점 (0, 0)을 포함하고 있는 직사각형이 있다면
그 그룹은 처음에 펜을 안떼고 그릴 수 있으므로 그룹의 개수에서 1을 빼준 것이 PU명령의 최솟값이다.

만약 그렇지 않다면, 그냥 그룹의 개수가 PU명령의 최솟값이다.

직사각형의 개수가 1000개로 주어지고, 시간 제한이 1초 이므로 O(n^2)의 시간 복잡도로 구현 가능하다.
'''

import sys
input = sys.stdin.readline

def is_two_rectangle_meet(rect1, rect2):
    if (rect1[1][0] < rect2[0][0] or rect2[1][0] < rect1[0][0] or
        rect1[0][1] > rect2[1][1] or rect2[0][1] > rect1[1][1]):  # 아예 만나지 않을 때
        return False
    elif ((rect1[0][0] < rect2[0][0] < rect2[1][0] < rect1[1][0] and
          rect1[0][1] < rect2[0][1] < rect2[1][1] < rect1[1][1]) or
          (rect2[0][0] < rect1[0][0] < rect1[1][0] < rect2[1][0] and
          rect2[0][1] < rect1[0][1] < rect1[1][1] < rect2[1][1])): # 면적이 겹치지만 안에 쏙 들어가있을 때
        return False
    else:
        return True
    
def is_contain_origin(rect):
    if (0 not in rect[0]) and (0 not in rect[1]):
        return False
    elif rect[0][0]*rect[1][0] > 0 or rect[0][1]*rect[1][1] > 0:
        return False
    else:
        return True
def find(node):
    if reps[node] != node:
        reps[node] = find(reps[node])
    return reps[node]
def union(node1, node2):
    rep1 = find(node1)
    rep2 = find(node2)
    reps[rep2] = rep1

N = int(input())
reps = list(range(N))
rects = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    rects.append(((x1, y1), (x2, y2)))

for i in range(N-1):
    for j in range(i+1, N):
        if is_two_rectangle_meet(rects[i], rects[j]):
            union(i, j)

for i in range(N):
    find(i)

total = len(set(reps))
for i in range(N):
    if is_contain_origin(rects[i]):
        total -= 1
        break

print(total)
