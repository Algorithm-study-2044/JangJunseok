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
    

#2차시도. 리트코드의 풀이 참고.
    
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.process(root, p, q)

    def process(self, node, p, q):
        if not node: 
            return node 
        
        # p, q중에 하나라도 node와 일치하면, 그냥 그 노드를 반환한다.
        if node == p or node == q: 
            return node
        
        # 만약 이 두 경우에 모두 해당하지 않으면, 그러면 왼쪽, 오른쪽을 탐색한다.

        #self.process는 그래서 뭐하는 함수인데? 
        #node.left, node.right를 탐색하면서, p, q가 있는지 확인하고,
        

        left = self.process(node.left, p, q)
        right = self.process(node.right, p, q)

        if left and right: 
            return node
        
        # right가 없고, left만 있는 경우.
        if left: 
            return left 
        
        if right: 
            return right