#1차 풀이 실패.

# 근데 이 풀이의 문제점은 그거다. 만약에 3,4이라는 놈이 만나서, 아 부모가 2에요! 라고 했는데,
# 그런데 이 2라는 놈이 만약에 1이랑 만나서 부모가 1로 갱신되어버렸다. 그러면 1,1,2,2 이렇게 되어버리니까.
# 그러니까 뒤에서 값이 갱신되어 버리면, 앞에서 갱신된 값들은 갱신이 안되는 것이다.

# [1,2,3] 이렇게 만든다.
# 작은것으로 바꾼다.
# 1인것들을 보고, 그것들의 부모를 통합한다. 
# 그런데 그 친구 입장에서 볼때 나랑 연결된 그 지점의 parent가 나보다 작은놈이다? 그러면 그놈으로 가야 한다.
# 그럼 가장 작은놈을 찾아서, 그 놈으로 다 바꿔줘야 하는것.



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected))] 

        for i in range(len(isConnected)):
            # parent값이 가장 가장 작은놈을 찾아서, 그놈으로 다 바꿔주자.
            min_val = parent[i]

            for idx, val in enumerate(isConnected[i]):
                if isConnected[i][idx] == 1 and parent[idx] < min_val:
                    # 연결되어있고 부모가 더 작으면, 그 부모를 더 작은걸로 만들고,
                    min_val = val

            for idx, val in enumerate(isConnected[i]):
                if isConnected[i][idx] == 1:
                    parent[idx] = min_val
        
        return len(set(parent))

# 2차 풀이. 이래도 틀렸음.

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            pa = find(x)
            pb = find(y)
            if pa < pb:
                parent[y] = pa
            else:
                parent[x] = pb
        
        for i in range(n):
            for j in range(i + 1, n):  
                if isConnected[i][j] == 1:
                    union(i, j)
        
        return len(set(find(i) for i in range(n)))
    
# 3차 풀이. dfs를 이용한 풀이.

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            for neighbor, connected in enumerate(isConnected[city]):
                if connected == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        n_provinces = 0
        visited = set()
        for city in range(len(isConnected)):
            if city not in visited:
                visited.add(city)
                dfs(city)
                n_provinces += 1

        return n_provinces