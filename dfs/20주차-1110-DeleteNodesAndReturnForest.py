# 1차시도 성공. 73ms. 5.17% beats.

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        res = []
        
        def DFS(node, parent, isLeft):
            if not node:
                return 
            
            if parent and node.val in to_delete:
                if isLeft:
                    parent.left = None
                else:
                    parent.right = None
            
            if node.val in to_delete:
                if node.left and node.left.val not in to_delete:
                    res.append(node.left)
                if node.right and node.right.val not in to_delete:
                    res.append(node.right)

            DFS(node.left, node, True)
            DFS(node.right, node, False)
        
        DFS(root, None, False)

        if root.val not in to_delete:
            res.append(root)

        return res
    

# 다른사람의 풀이.

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        s = set(to_delete)
        res = []
        def dfs(root, flag):
            if not root: return None
            toDelete = (root.val in s)
            root.left = dfs(root.left, toDelete)
            root.right = dfs(root.right, toDelete)
            if not toDelete and flag: res.append(root)
            return None if toDelete else root
        dfs(root, True)
        return res
        