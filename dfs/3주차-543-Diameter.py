#3주차. 시간초과. 다시풀것.
#3주차. 2차시도. 22분 소요. pass. 57% beats.

class Solution(object):
    def diameterOfBinaryTree(self, root):
        result = []
        def DFS(node):
            if not node:
                return 0
            if node.left:
                leftVal = DFS(node.left) + 1
            else:
                leftVal = 0
            if node.right:
                rightVal = DFS(node.right) + 1
            else:
                rightVal = 0

            result.append(leftVal+rightVal)
            return max(leftVal, rightVal)

        DFS(root)
        return max(result)