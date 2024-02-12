#3주차. pass. 5분 소요. 18ms. 30% beats.
class Solution(object):
    def isSameTree(self, p, q):
    
        def DFS(p,q):
            if not p and not q:
                return True
            elif p and not q:
                return False
            elif q and not p:
                return False
            else:
                return p.val == q.val and DFS(p.left, q.left) and DFS(p.right, q.right)

        return DFS(p,q)
        