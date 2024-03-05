# 6주차. 1차시도. 17분 소요. 36ms. 21% beats.

class Solution(object):
    def removeLeafNodes(self, root, target):
        def isLeaf(node):
            return node.left == None and node.right == None

        def DFS(node):
            if node.left:
                node.left = DFS(node.left)
            if node.right:
                node.right = DFS(node.right)
            
            if node.val == target and isLeaf(node):
                return None
            else:
                return node
        
        root = DFS(root)

        return root