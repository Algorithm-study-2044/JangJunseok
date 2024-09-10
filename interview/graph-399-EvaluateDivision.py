# 8:14 시작.

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph={}

        for eq,value in zip(equations,values):
            if eq[0] not in graph: graph[eq[0]]={}
            if eq[1] not in graph: graph[eq[1]]={}
            graph[eq[0]][eq[1]]=value
            graph[eq[1]][eq[0]]=1/value
        
        def DFS(src, dest, seen):
            if src not in graph or dest not in graph:
                return -1

            if src == dest:
                return 1

            seen.add(src)
            
            # 그럼 못찾았다는거는 어떻게 알 수 있는데? 모든곳을 재귀 돌면,
            # 여러 루트중에서 result에 들어가는건 뭔데?

            # 그리고 한번 왔다는것도 어떻게 알 수 있는데?
            # seen을 활용해서, 근데 seen은 어떻게 되는건데?
            # 시작점만 기록하면 된다. 이건 양방향 나눗셈인데도?
            
            for neigh, val in graph[src].items():
                if neigh not in seen:
                    result = DFS(neigh,dest,seen)
                    if result != -1:
                        return result * val
            return -1
        
        res = []
        for start, end in queries:
            res.append(DFS(start,end,set()))
        return res

# 2차 시도. 다른사람의 풀이 참조.

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph={}

        for eq,value in zip(equations,values):
            if eq[0] not in graph: graph[eq[0]]={}
            if eq[1] not in graph: graph[eq[1]]={}
            graph[eq[0]][eq[1]]=value
            graph[eq[1]][eq[0]]=1/value

        
        def dfs(src,dst,visited):
            if src not in graph or dst not in graph: return -1
            if src==dst: return 1
            visited.add(src)
            for neighbour,value in graph[src].items():
                if neighbour not in visited:
                    result=dfs(neighbour,dst,visited)
                    # a/b = 3이고 b/c = 2 라고 한다면. a/c는 얼마에요?
                    # 그 전에 나온 값에다가 이번에 나온 값을 곱해주면 될 거다.
                    # 근데 내가 막혔던거는. 이거 그러면 값 업데이트 이런거 안해줘도 되는건가?
                    if result!=-1: return result*value
            return -1
        
        results=[]
        for query in queries: results.append(dfs(query[0],query[1],set()))
        return results
    

# 다른 사람의 풀이 다시 참고.
# 그래프를 만드는것 자체는 동일함.

from typing import List

class Solution:
    def dfs(self, node: str, dest: str, gr: dict, vis: set, ans: List[float], temp: float) -> None:
        if node in vis:
            return

        vis.add(node)
        if node == dest:
            ans[0] = temp
            return

        # 이거는 뭐랄까. 시작부터 끝까지 계산하는 느낌이라면,
        # DFS는 끝에서, val구하고, 그 다음에 그 val을 다시 다음 val에 더하고,
        for ne, val in gr[node].items():
            self.dfs(ne, dest, gr, vis, ans, temp * val)

    def buildGraph(self, equations: List[List[str]], values: List[float]) -> dict:
        gr = {}

        for i in range(len(equations)):
            dividend, divisor = equations[i]
            value = values[i]

            if dividend not in gr:
                gr[dividend] = {}
            if divisor not in gr:
                gr[divisor] = {}

            gr[dividend][divisor] = value
            gr[divisor][dividend] = 1.0 / value

        return gr

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        gr = self.buildGraph(equations, values)
        finalAns = []

        for query in queries:
            dividend, divisor = query

            if dividend not in gr or divisor not in gr:
                finalAns.append(-1.0)
            else:
                vis = set()
                ans = [-1.0]
                temp = 1.0
                self.dfs(dividend, divisor, gr, vis, ans, temp)
                finalAns.append(ans[0])

        return finalAns

# 8:14 시작.

# a와 b가 있고, b와 c가 있을때, 
# a와 c의 값을 구할 수 있나.

# 그런데 a와 c를 연결할때 하나의 값이 있는게 아니라,
# 방향에 따라서 값이 다르다.

# b에서 c로 가는거 들어오면,
# 기존에 a에서 b로 가는게 있었으니까,
# b랑 c랑 큐에 넣어놓고,

# (a,b,2) (b,c,3) 이렇게 있으면
# a -> {b -> 2}
# b -> {a -> 1/2, c -> 3} 이렇게 넣어두고
# c -> {b -> 1/3}

# b도 마찬가지로 넣어두고,
# 나중에 b,c가 들어오면?
# b랑 c랑 큐에 넣어두고,

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        print("i don't know..")

