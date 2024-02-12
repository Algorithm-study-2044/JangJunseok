#3주차. 1차시도. 시간초과 fail. 비대칭일때 케이스 분류가 헷갈린다.

class Solution(object):
    def invertTree(self, root):    

        def changeNode(l, r):
            if not l and not r:
                return
            elif l and not r:
                r = TreeNode(l.val, l.left, l.right)
                l = None
                changeNode(None, r.right)
                changeNode(None, r.left)
            elif not l and r:
                l = TreeNode(r.val, r.left, r.right)
                r = None
                changeNode(l.left, None)
                changeNode(l.right, None)
            else:   
                left_val = l.val
                l.val = r.val
                r.val = left_val
                changeNode(l.left, r.right)
                changeNode(l.right, r.left)
                

            
            #둘다 있을때. val끼리 교체.
            #하나만 있을때. 하나는 val에다가 넣고, 하나는 None으로 만들기
            #
        if root:
            changeNode(root.left,root.right)
    
        return root
