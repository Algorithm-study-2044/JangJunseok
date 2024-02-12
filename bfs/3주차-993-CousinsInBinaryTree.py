#3주차. pass. 12분 소요. 12ms. 81% beats.

class Solution(object):
    def isCousins(self, root, x, y):
        result = []
        def DFS(node, depth, parent):
            if len(result) == 2 or not node:
                return
            depth += 1
            if node.val == x or node.val == y:
                result.append((depth,parent))
            
            DFS(node.left,depth,node)
            DFS(node.right,depth,node)
            
        DFS(root,0,None)
        return result[0][0] == result[1][0] and result[0][1].val != result[1][1].val