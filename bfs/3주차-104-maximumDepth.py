#3주차. pass. 17ms. 90% beats.

class Solution(object):
    def maxDepth(self, root):
        maxDepVal = [0]
        def DFS(node,depth):
            if not node:
                return
            depth += 1
            if maxDepVal[0] < depth:
                maxDepVal[0] = depth
            if node.left:
                DFS(node.left,depth)
            if node.right:
                DFS(node.right,depth)

        DFS(root,0)
        return maxDepVal[0]