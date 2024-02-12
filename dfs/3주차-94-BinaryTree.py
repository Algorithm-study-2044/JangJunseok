#3주차. 10분 소요. pass. 15ms. 51% beats.
# 다른 풀이가 있는지.

class Solution(object):
    def inorderTraversal(self, root):
        result = []
        def DFS(node):
            if not node:
                return
            if node.left:
                DFS(node.left)
            result.append(node.val)
            if node.right:
                DFS(node.right)
        DFS(root)
        return result
        