# 나의 풀이. 6440ms. 5% beats.

from heapq import heappush, heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def calcCost(a,b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])

        n = len(points)
        parent = list(range(n))

        heap = []
        for i in range(n):
            for j in range(n):
                heappush(heap,(calcCost(points[i],points[j]),i,j))
        
        # 0,1번을 union하면 되는거다!
        def find_parent(x):
            if x != parent[x]:
                parent[x] = find_parent(parent[x])
            return parent[x]
        
        def union_parent(x,y):
            px = find_parent(x)
            py = find_parent(y)

            if px > py:
                parent[py] = px
            else:
                parent[px] = py

        total = 0

        while heap:
            dist,pointA,pointB = heappop(heap)
            if find_parent(pointA) != find_parent(pointB):
                total += dist
                union_parent(pointA, pointB)

        return total
        
            

# 다른 사람의 풀이.

def manhattan_distance(p1: List[int], p2: List[int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        
    def find(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        
        if u == v:
            return False
        
        if self.rank[u] > self.rank[v]:
            u, v = v, u
            
        self.parent[u] = v
        
        if self.rank[u] == self.rank[v]:
            self.rank[v] += 1
        
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)
        
        edges = []
        
        for i in range(n):
            for j in range(i+1, n):
                distance = manhattan_distance(points[i], points[j])
                heappush(edges, (distance, i, j))
        
        mst_weight = 0
        mst_edges = 0
        
        while edges:
            w, u, v = heappop(edges)
            if uf.union(u, v):
                mst_weight += w
                mst_edges += 1
                if mst_edges == n - 1:
                    break
                    
        return mst_weight