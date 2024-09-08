# 다른 사람의 풀이 참고.

# 일단 dfs로 접근하는 이유. 
# 어느 점에서 , 그걸로 인해 다른게 영향을 받아버린다.
# 밑에 풀이는, 어느 점에서 시작하든 다 지워버린다.

# 왜? insights는, 어느 지점에서 시작하든, 하나 빼고 다 지울 수 있다는 것에서 시작한다.
# 그러니까 굳이 어느 점에서 시작하냐..이걸 고려할 필요가 없다는 것이다.

# 혼자 있는 애들은 group으로 묶이겠지. 그리고 연결되어있는 놈들은, 다 지뢰찾기 처럼 제거가 될거다.
# 일단 제거만 되면 된다. 그러니까 거기서 순서를 고려할 필요가 없다. 왜? 그냥 순차적으로 제거한다고 가정하면 되는거니까,

# 근데 왜 n - group인가?
# group의 개수만큼. 남는 돌이 있고, 나머지는 다 제거할 수 있으니까, n - group이다.
# group에는 항상 1개만 남는다는 것이다.

class Solution(object):
    def dfs(self, n, idx, visited, stones):
        visited[idx] = True
        for i in range(n):
            if not visited[i]:
                if stones[idx][0] == stones[i][0]:
                    self.dfs(n, i, visited, stones)
                if stones[idx][1] == stones[i][1]:
                    self.dfs(n, i, visited, stones)

    def removeStones(self, stones):
        n = len(stones)
        group = 0
        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                group += 1
                self.dfs(n, i, visited, stones)
        return n - group 
    



# 1차시도.

# 같은 row or column인경우에,
# 연결점이 가장 적은놈들부터 제거해가면 되긴 한데,

# 같은 선상에 있을때, 어느것을 지워야 하는가? 
# 사실 둘다 서로 연결되어있다면 뭐 의미가 없는데,

# 둘중 하나가 둘다 연결되어있는 경우에는, 그걸 나중에 제거해야함.
# 1개만 연결되어 있는 경우는 무조건 

# x_dict와 y_dict를 만든다음에, 각 좌표를 저장하고,
# 또 다시 한번 돌면서, 힙에 넣어주고, 어떤순으로? 연결된 순의 개수가 0이냐? 1이상이냐?
# 0 이면 넣지 않고, 1이상부터는 넣어준다.
# 그 다음에 하나씩 뽑아준다. 뽑은 거 카운터에서 지우고,

# 근데 이렇게 하면 보장할 수가 없다. 같은거중에서 누구를 먼저 지울지. 
# 재귀를 써서 풀어야 하나?

import heapq

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        x_dict = defaultdict(int)
        y_dict = defaultdict(int)

        for x,y in stones:
            x_dict[x] += 1
            y_dict[y] += 1
        
        hp = []
        for x,y in stones:
            points = x_dict[x] + y_dict[y]
            heapq.heappush(hp,[points,x,y])
        
        cnt = 0
        while hp:
            points,x,y = heapq.heappop(hp)
            if x_dict[x] >= 2 or y_dict[y] >= 2:
                cnt += 1
                x_dict[x] -= 1
                y_dict[y] -= 1
        
        return cnt
    
