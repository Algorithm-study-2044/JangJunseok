# 8:09. 17분 소요. 

# [1,2] [0,1] 이렇게 있으면
# 0에서 2 갈 수 있나?
# 그냥 map을 만들면 어떨까? 0->[1,2] 1->[2,0]
# 근데 이러면, 순환할 가능성이 있다.

# 그러면 union-find를 써야 하나?
# 둘이 부모가 같으면 연결되어 있는 것으로?


# 이렇게 하면 시간초과. 시간초과인데 왜???

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = list(range(n))
        def find(t):
            if t != parent[t]:
                # 이렇게 하면 t의 대표 부모를 찾기는 찾는데, 할때마다 건드려야 하니까
                return find(parent[t])
            return t

        def union(x,y):
            px = find(x)
            py = find(y)
            if px >= py:
                parent[py] = px
            else:
                parent[px] = py
        
        for p,q in edges:
            union(p,q)
        
        if find(source) == find(destination):
            return True
        return False


# 경로 압축을 하지 않았다. 
# 이렇게 하면 2396ms. 99.41% beats.

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = list(range(n))
        

        # if t != parent[t]:
            # 이렇게 하면 t의 대표 부모를 찾기는 찾는데, 할때마다 건드려야 하니까
            # return find(parent[t])

        # 근데 이 친구는 한번 하면 t의 대표 부모를 업데이트 가능하고, 그 대표부모 사이에 있는 노드들도 다 대표부모로 업데이트가 된다.
        # 그러므로 경로압축이라고 할 수 있음.
        def find(t):
            if t != parent[t]:
                parent[t] = find(parent[t])
            return parent[t]

        def union(x,y):
            px = find(x)
            py = find(y)
            if px >= py:
                parent[py] = px
            else:
                parent[px] = py
        
        for p,q in edges:
            union(p,q)
        
        if find(source) == find(destination):
            return True
        return False
        