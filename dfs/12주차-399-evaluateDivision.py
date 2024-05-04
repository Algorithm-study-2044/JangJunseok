#2:55 DFS로 시도. 1차시도. 실패.

# a/b = 2.0
# b/c = 3.0
# a = 2b
# a=2b. b=3c. 

# 그러면 a/c가 주어졌을때, a를 DFS해서 바꿔본다.
# 2b/c일테고, 만약 안똑같다? 그러면 그 다음.

# [a,b,c,d] 있을때, a->b->c->d랑
# b -> c -> d 도 있을거고.

class Solution(object):
    def calcEquation(self, equations, values, queries):
        
        res = [-1.0] * len(queries)
        dic = {}

        for i in range(len(equations)):
            right = equations[i][1]
            left = equations[i][0]
            dic[right] = (left,1/values[i])
            dic[left] = (right,values[i])
            
        def DFS(a,b,eq,i):
            if a == b[0]:
                res[i] = b[1]
                return
            if not eq:
                return
            if b[0] in dic and a == dic[b[0]][0]:
                res[i] = dic[b[0]][1]
                return

            else:
                for j in eq[1:]:
                    DFS(a,dic[j[1]],eq[1:],i)

        for idx, k in enumerate(queries):
            DFS(k[0],(k[1],1),equations,idx)

        return res
    

# 2차시도. 다른 사람의 풀이 참고해서 풀었음.

class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)
    
        for (u,v),val in zip(equations,values):
            graph[u][u] = 1
            graph[v][v] = 1
            graph[u][v] = val
            graph[v][u] = 1/val

        # k/i = 3 (graph[k][i]) k/j = 2 (graph[k][j])
        # i/j는 어떻게 구하나?
        # k / graph[k][i] // k / graph[k][j]
        # graph[k][j] / graph[k][i] 인데,
        # 이때 graph[k][i] 값은 graph[i][k]와 같으므로,

        for k in graph:
            for i in graph[k]:
                for j in graph[k]:
                    graph[i][j] = graph[k][j] * graph[i][k]
        # 파생된 것 끼리도 답을 찾아준다.

        #그 다음에. 이제 정답이 있는지 없는지 찾아주면 됨.
        for (u,v) in queries:
            return [graph[u].get(v,-1) for u,v in queries]
