from bisect import bisect_left

# 37ms. 52.42% beats.

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        all_keys = []

        def DFS(node):
            if not node:
                return

            all_keys.append(node.val)
            DFS(node.left)
            DFS(node.right)
        
        DFS(root)
        all_keys.sort()
        all_points = all_keys[::]
        res = 0

        for i in range(len(all_keys)-1,-1,-1):
            res += all_keys[i]
            all_points[i] = res
                
        def DFS_2(node):
            if not node:
                return
            idx = bisect_left(all_keys,node.val)
            node.val = all_points[idx]
            DFS_2(node.left)
            DFS_2(node.right)

        DFS_2(root)

        return root
    
# 그냥 이렇게 해도 된다. BST의 속성 활용.

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.val = 0
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.right)
            self.val += node.val
            node.val = self.val
            dfs(node.left)
        
        dfs(root)
        return roo