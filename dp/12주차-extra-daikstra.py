#daikstra 알고리즘의 구현.

path  = [
    [0,1,2,3,inf,inf],
    [0,1,2,3,inf,inf],
    [0,1,2,3,inf,inf],
    [0,1,2,3,inf,inf],
    [0,1,2,3,inf,inf],
    [0,1,2,3,inf,inf],
]

visited = [0] * 6
dist = [0] * 6



def getMinPathIndex(dist):
    
    min = inf
    index = 0
    for i in range(len(dist)):
        if dist[i] < min and not visited[i]:
            index = i

    return index

def daikstra(start):
    
    for i in range(len(path)):
        # 일단 이렇게 거리를 초기화시켜놓고
        dist[i] = path[start][i]
    
    visited[start] = 1

# 왜 여기서는 number-2번 만큼 반복해야하는건가?
# 0은 이미 갔으니까 그럴 필요 없다치고.

    for i in range(len(path)-2):
        next_idx = getMinPathIndex(dist)
        visited[next_idx] = 1

        for j in range(len(path)):
            if not visited[i]:
                if dist[next_idx] + path[next_idx][j] < dist[j]:
                    dist[j] = dist[next_idx] + path[next_idx][j]
    
    
print()

