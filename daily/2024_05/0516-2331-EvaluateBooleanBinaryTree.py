# 6;05. 7분 소요.

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def DFS(node):
            if node.val == 1 or node.val == 0:
                return node.val

            left = DFS(node.left)
            right = DFS(node.right)

            if node.val == 2:
                return left or right

            if node.val == 3:
                return left and right
        
        return DFS(root)