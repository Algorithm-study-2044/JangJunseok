
# 10:43 시작. 11:15분. 32분 소요.
# 테스트케이스는 다 통과했는데, 틀렸다고 나옴...

# 전략.
# 그냥 처음 점에서는 방향을 틀면 안됨.
# 그런데 다른걸 만났다? 그러면 그 점에서 이제
# 기존 방향과 다른 3방향을 본 다음에, 
# 거기에 똑같은 색이 있었다? 글면. +1한걸 max 비교.
# 아니면 그냥 기존 길이를 max 비교.

import sys

n = int(input())
arr = []
res = [0]

for _ in range(n):
    df = list(sys.stdin.readline().strip())
    arr.append(df)

px = [0,0,1,-1]
py = [1,-1,0,0]


def isNotInArr(it):
    x, y = it
    return x < 0 or x >= len(arr) or y < 0 or y >= len(arr[x])


# 어떻게 보면 cnt는 이전까지의 길이를 의미함.
def DFS(initial,way,before_color,cnt):
    x,y = initial
    dx,dy = way
    if isNotInArr((x,y)):
        res[0] = max(res[0],cnt)
        return

    curr = arr[x][y]

    if curr != before_color:
        # 여기서 기존 dx,dy를 제외한 3방향을 비교.
        # 거기에 before_color가 있다? 그러면
        # cnt += 1 한다음에, max 비교.
        # 없다? 그러면 그냥 max 비교.r

        flag = False
        for i in range(4):
            nx,ny = px[i],py[i]
            if nx == dx and ny == dy:
                continue
            if isNotInArr((x+nx,y+ny)):
                continue
            if arr[x+nx][y+ny] == before_color:
                flag = True
            
        if flag:
            cnt += 1

        res[0] = max(res[0],cnt)

    else:
        # 색이 같다? 그러면 길이 늘려준다음에,
        #다시 넣어준다.
        cnt += 1
        DFS((x+dx,y+dy),(dx,dy),curr,cnt)


for i in range(len(arr)):
    for j in range(len(arr[i])):
        # 시작 cnt 는 0
        # 시작 컬러는 해당 컬러와 같게 시작.
        # 방향은 4방향으로.
        for k in range(4):
            DFS((i,j),(px[k],py[k]),arr[i][j],0)

print(res[0])




# 2차시도. 다른 사람의 풀이 참고.

def get_max_candies(board, n):
    max_candies = 1

    # 연속된 같은 색의 사탕 개수 세기
    def count_candies(arr):
        nonlocal max_candies

        # 해당 row별로, 가로로 가장 긴걸 찾아준다. 어떻게? 일단 0번 기준으로.
        for row in arr:
            current_color = row[0]
            count = 1
            for i in range(1, n):
                if row[i] == current_color:
                    count += 1
                else:
                    max_candies = max(max_candies, count)
                    current_color = row[i]
                    count = 1

            # 마지막에도 해줘야 한다. 왜? 아니면 계속 가다가 멈춰버리니까.
            max_candies = max(max_candies, count)
        
        # col을 결정한다는건, arr[x][여기]를 고정시켜준다는 말.
        for col in range(n):
            current_color = arr[0][col]
            count = 1
            for i in range(1, n):
                if arr[i][col] == current_color:
                    count += 1
                else:
                    max_candies = max(max_candies, count)
                    current_color = arr[i][col]
                    count = 1
            max_candies = max(max_candies, count)

    # 두 칸의 사탕 교환 후 최대 연속 부분 찾기
    for i in range(n):
        for j in range(n):
            if j + 1 < n:
                # 가로로 인접한 사탕 교환
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                count_candies(board)
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

            if i + 1 < n:
                # 세로로 인접한 사탕 교환
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                count_candies(board)
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

    return max_candies


n = int(input())
board = [list(input().strip()) for _ in range(n)]
print(get_max_candies(board, n))
