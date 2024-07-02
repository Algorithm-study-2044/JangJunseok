# 2차시도. 다른 사람의 풀이 참고.
# 부모, 자식, 손자 이렇게 있을때

# 나의 접근은, 각 edges별로 돌면서, 부모의 부모를 다 넣어주고, 자식들도 다시 업데이트하는 방식이었다.
# 그리고 이렇게 해서 넣어진 자식들의 경우에는, 또 sort를 해줘야 했고.

# 굳이 edges에 집착할 필요가 없다는 것이다. 

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        direct_child = [[] for _ in range(n)]
        ans = [[] for _ in range(n)]
        for e in edges:
            direct_child[e[0]].append(e[1])
        for i in range(n):
            self.DFS(i,i,direct_child,ans)
        return ans
        
    def DFS(self,top_parent,current,direct_child,ans):
        for child in direct_child[current]:
            if not ans[child] or ans[child][-1] != top_parent:
                ans[child].append(top_parent)
                self.DFS(top_parent,child,direct_child,ans)


# 1차시도. 시간 초과.

class TreeNode:
    def __init__(self, value):
        self.parent = set()
        self.child = set()
        self.value = value

from collections import deque

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        gone = set()
        nodes = [None] * n

        for i in range(n):
            node = TreeNode(i)
            nodes[i] = node
        

        edges = deque(edges)

        while edges:
            cnt = len(edges)
            for _ in range(cnt):
                start,end = edges.popleft()
                nodes[start].child.add(end)
                nodes[end].parent.add(start)

                # 부모의 부모를 다 넣어주고,
                for grandparent in nodes[start].parent:
                    nodes[end].parent.add(grandparent)

                # 자식들도 다시 업데이트한다.
                for child in nodes[end].child:
                    edges.append((end,child))

        
        res = []
        for node in nodes:
            res.append(sorted(node.parent))
        
        return res
    
