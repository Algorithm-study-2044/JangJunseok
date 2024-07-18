# 8분 소요. 41ms. 71% beats.

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        level = []
        
        def BFS(top):    
            queue = deque([(top,0)])
            while queue:
                node,lv = queue.popleft()
                if len(level) <= lv:
                    level.append(node.val)
                elif level[lv] < node.val:
                    level[lv] = node.val

                if node.left:
                    queue.append((node.left,lv+1))
                if node.right:
                    queue.append((node.right,lv+1))
        
        BFS(root)
        return level




        


