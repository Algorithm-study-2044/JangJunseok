# 3주차. pass. 189ms. 52% beats.

class Solution(object):
    
    def DFS(self, node, low, high, result):
        if node is None:
            return
        if node.val >= low and node.val <= high:
            result[0] += node.val
        if node.left:
            self.DFS(node.left, low, high, result)
        if node.right:
            self.DFS(node.right, low, high, result)

    def rangeSumBST(self, root, low, high):
        result = [0]
        self.DFS(root,low,high, result)
        return result[0]
    

class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        ans=0
        def preOrder(root, low, high):
            nonlocal ans
            if not root: return
            if low<=root.val<=high:
                ans+=root.val
            preOrder(root.left, low, high)
            preOrder(root.right, low, high)
        
        preOrder(root, low, high)
        return ans