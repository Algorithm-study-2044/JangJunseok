# 06:46 시작. 06 55분. 9분 소요.

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def DFS(node,isLeft):
            if not node:
                return 0

            if not node.left and not node.right and isLeft:
                return node.val

            left = DFS(node.left,True)
            right = DFS(node.right,False)

            return left + right

        return DFS(root,False)



        