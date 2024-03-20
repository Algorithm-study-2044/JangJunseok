# 1차시도. 성공. 시간많이걸림. 근데 왜 distance를 1 더 더해주어야 하는가? 시작점도 1이니까.

res = []

R, C, K = map(int,input().split())

def DFS(x,y,arr,distance):

    newarr = arr[:]

    if x == C-1 and y == 0:
        res.append(distance)
        return
    
    if x < 0 or x > C-1 or y < 0 or y > R-1:
        return

    curr = arr[y][x]

    if curr == "T" or curr == "d":
        return

    elif curr == ".":
        arr123 = list(newarr[y])
        arr123[x] = "d"
        newarr[y] = "".join(arr123)

    moveX = [0,0,-1,1]
    moveY = [-1,1,0,0]    
    
    for i in range(4):
        nextX = x + moveX[i]
        nextY = y + moveY[i]
        DFS(nextX, nextY, newarr, distance+1)

arr = []

for _ in range(R):
    arr.append(input())


DFS(0,R-1,arr,1)

print(res.count(K))
