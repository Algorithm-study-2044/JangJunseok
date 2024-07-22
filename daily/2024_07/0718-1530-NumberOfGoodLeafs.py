# 8:01 시작. 24분 소요. 221ms. 17.70% beats.

from itertools import product
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = [0]
        def DFS(node):
            if not node:
                return

            left = DFS(node.left)
            right = DFS(node.right)

            if not left and not right:
                return [[node.val,1]]
            
            elif left and right:
                comb = product(left,right)
                for item in comb:
                    if item[0][1] + item[1][1] <= distance:
                        res[0] += 1
                alls = [*left,*right]
                for item in alls:
                    item[1] += 1
                return alls
            elif left:
                for item in left:
                    item[1] += 1
                return left
            elif right:
                for item in right:
                    item[1] += 1
                return right

        DFS(root)
        return res[0]