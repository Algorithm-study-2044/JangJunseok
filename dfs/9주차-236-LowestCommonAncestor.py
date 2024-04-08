# 1차 시도. 22분 소요. 43ms. 73% beats.

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        
        # 여기에는 각 node val의 depth를 저장한다.
        _depth = {}
        # 자식이 key, 부모가 value로 설정한다.
        graph = {}

        def DFS(node, parent, depth):
            if not node:
                return
            
            _depth[node.val] = depth
            if parent:
                graph[node.val] = parent

            DFS(node.left, node, depth+1)
            DFS(node.right, node, depth+1)
        
        DFS(root, None, 0)

        curr_p = p
        curr_q = q

        while curr_p.val != curr_q.val:
            if _depth[p.val] == _depth[q.val]:
                _depth[p.val] -= 1
                _depth[q.val] -= 1
                curr_p = graph[curr_p.val]
                curr_q = graph[curr_q.val]
            elif _depth[p.val] > _depth[q.val]:
                _depth[p.val] -= 1
                curr_p = graph[curr_p.val]
            else:
                _depth[q.val] -= 1
                curr_q = graph[curr_q.val]
        
        return curr_p
    


    
# 리트코드의 풀이.
 
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.process(root, p, q)

    def process(self, node, p, q):
        if not node: 
            return node 
        
        if node == p or node == q: 
            return node

        left = self.process(node.left, p, q)
        right = self.process(node.right, p, q)

        if left and right: 
            return node
        
        if left: 
            return left 
        
        if right: 
            return right
        
    

# 민호님 풀이.

class Solution:
    LCA = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, p, q):
            if node is None:
                return node
            
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)

            if node.val == p.val or node.val == q.val:
                if left or right:
                    self.LCA = node
                return node
            
            elif left and right:
                self.LCA = node
                return node
            
            return left or right
        
        dfs(root, p, q)
        
        return self.LCA