# 1차시도. 크루스칼 알고리즘 참고. 4816ms. 17% beats.

# 크루스칼 알고리즘을 사용.
# 각 간선의 비용을 계산한 뒤, 
# 그거 오름차순으로 정렬하고, 그리고 그것 중에서 
# 사이클이 발생하지 않는 경우에만 넣어준다.

# 다익스트라는 특정 정점에서 다른 점으로 가는 최단 경로를 계산하는것임.
# 0에서 시작해서, 그 다음 1로 가고, 해당 1에서 갈 수 있는 최단경로를 다 업데이트해주고,

class Solution(object):
    def minCostConnectPoints(self, points):

        def calcCost(a,b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])

        n = len(points)
        edges = []
        parent = list(range(n))
        total = 0

        def find_parent(parent,a):
            if parent[a] != a:
                # parent[a]의 제일 조상을 찾아서
                # 그거를 parent[a] 값에다가 넣어준다.
                parent[a] = find_parent(parent,parent[a])
            return parent[a]

        def union_parent(parent,a,b):
            # a,b idx가 있을때, 각각의 
            pa = find_parent(parent,a)
            pb = find_parent(parent,b)

            # 그런데 왜 parent[a]가 아니라 parent[pa]인걸까?
            # 생각해봐라, 각각의 부모자식이 있고, 자식들끼리 결합할때, 자식들만 바꿔주면 되나? 안된다.
            # 그 조상을 찾아서 걔네들끼리 맞다이를 시켜줘야지.

            # 그러면 parent[a]는 안바뀌어도 된다. 왜냐하면 여전히 이전의 부모를 참조하고 있지만,
            # 이제는 그 부모가 다시 pb즉 b의 부모가 되어버렸기 때문이다.
            if pa > pb:
                parent[pa] = pb
            else:
                parent[pb] = pa

        for i in range(n):
            for j in range(n):
                edges.append((calcCost(points[i],points[j]),i,j))
        
        edges.sort()

        for i in range(len(edges)):
            cost,a_idx,b_idx = edges[i]
            if find_parent(parent, a_idx) != find_parent(parent,b_idx):
                # 사이클 발생 안함.
                # 그런데 여기서 idx,idx끼리 visited를 판단할 필요가 있을까?
                # 그 다음에 두 포인트의 parent를 합쳐줄 필요가 있다. 왜? 안그러면 판단이 안되니까
                union_parent(parent,a_idx,b_idx)
                total += cost
    
        return total
                


    
