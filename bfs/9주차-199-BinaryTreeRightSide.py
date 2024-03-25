from collections import deque

class Solution(object):
    def rightSideView(self, root):

        depth_dict = {}
        
        def BFS(root):
            queue = deque([(root,0)])

            while queue:
                curr,depth = queue.popleft() 
                if not curr:
                    continue
                else:
                    depth_dict[depth] = curr.val
                    queue.append((curr.left,depth+1))
                    queue.append((curr.right,depth+1))
        
        BFS(root)


        return depth_dict.values()