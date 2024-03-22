# 1차시도. 30분. 너무 느리다. 40ms. 85% beats.

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def DFS(node,distance):
            if not node:
                return distance -1

            left = DFS(node.left,distance+1)
            right = DFS(node.right,distance+1)

            if not left or not right:
                return False

            if abs(left-right) > 1:
                return False
            else:
                return max(left,right)
        
        if not root:
            return True

        return abs(DFS(root.left,1) - DFS(root.right,1)) <= 1 and DFS(root,1)