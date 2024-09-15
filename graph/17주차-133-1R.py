# 31ms. 96.14% beats.

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        gone = set()
        node_dict = {}

        def find_or_create(node):
            if node.val in node_dict:
                return node_dict[node.val]
            newNode = Node(node.val,None)
            node_dict[newNode.val] = newNode
            return newNode

        def travel(origin_node):
            if origin_node.val in gone:
                return
            gone.add(origin_node.val)
            new_node = find_or_create(origin_node)

            for neigh in origin_node.neighbors:
                new_neigh = find_or_create(neigh)
                new_node.neighbors.append(new_neigh)
                travel(neigh)
        
        travel(node)
        return node_dict[node.val]