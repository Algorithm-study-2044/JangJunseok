# BFS, DFS 모두 시간초과가 난다..
# set이 아니라 visited로 하면 시간초과가 나지 않는다. 왜? 
# 어차피 알파벳이라서? 26개밖에 없으니까?
import sys

R,C = map(int,sys.stdin.readline().split())
mat = []
for _ in range(R):
    mat.append(list(sys.stdin.readline()))

res = 0
seen = set()

def DFS(coord,cnt):
    global res
    x,y = coord
    if y < 0 or y >= len(mat) or x < 0 or x >= len(mat[y]) or mat[y][x] in seen:
        res = max(res,cnt)
        return
    cnt += 1
    seen.add(mat[y][x])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for i in range(4):
        next_coord = (x+dx[i], y+dy[i])
        DFS(next_coord,cnt,seen)
    
    seen.remove(mat[y][x])

DFS((0,0),0)

print(res)



# 1. set과 visited 리스트의 차이
# set의 특성
# set은 Python에서 해시 테이블 기반의 자료 구조로, 특정 요소의 존재 여부를 확인하거나 추가 및 제거하는 데 평균적으로 O(1)의 시간 복잡도를 가집니다.
# 하지만, set은 동적으로 크기가 변할 수 있는 자료 구조이기 때문에, DFS에서 깊은 재귀 호출이 이루어질 때, set의 상태를 계속해서 복사하거나 관리해야 합니다. 이 과정에서 추가적인 메모리 사용과 연산 비용이 발생합니다.
# 특히, 각 재귀 호출에서 set을 복사할 경우, 호출 깊이에 따라 복사 비용이 누적되어 성능에 큰 영향을 미칠 수 있습니다.
# visited 리스트의 특성
# visited 리스트는 고정된 크기(26)로, 각 알파벳에 대해 방문 여부를 추적합니다. 리스트의 크기는 항상 26으로 고정되어 있기 때문에, 각 연산의 시간 복잡도는 O(1)입니다.
# visited 리스트는 미리 정해진 크기를 가지고 있으므로, 메모리 복사나 동적 관리가 필요하지 않으며, 따라서 재귀 호출 시에도 성능이 매우 안정적입니다.
