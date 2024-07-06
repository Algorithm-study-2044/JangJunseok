# 38ms. 74.29% beats.

# 1에서 시작해서,
# 해당 val로 만들고,
# neightbor를 다 넣어준다.
# 그런데 만약에 dict에 만들어둔게 있으면, 그거 가져다 넣어주고
# 즉 find or create

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        gone = set()
        nodes = {}

        if not node:
            return None

        def find_or_create(node,nodes):
            if node.val in nodes:
                copy = nodes[node.val]
            else:
                copy = Node(node.val,None)
                nodes[node.val] = copy
            return copy
        
        def DFS(node):
            if node.val in gone:
                return
            gone.add(node.val)

            copy = find_or_create(node,nodes)
            
            for neigh in node.neighbors:
                neigh_copy = find_or_create(neigh,nodes)
                copy.neighbors.append(neigh_copy)
                DFS(neigh)
        
        DFS(node)
        return nodes[node.val]