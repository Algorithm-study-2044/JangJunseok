# 이 코드의 문제점은, 더 안내려가도록 선택할 수 있다는 점이다.
# 굳이 내려가서 계산할 필요가 없다는 것. 특히 [2,-1]에서 그렇다.

class Solution(object):
    def maxPathSum(self, root):
        res = [float("-inf")]

        def DFS(node):
            if not node:
                return 0

            left = DFS(node.left)
            right = DFS(node.right)
            total = node.val + left + right
            res[0] = max(res[0], total)

            return total

        DFS(root)

        return res[0]
    

# 2차시도.

class Solution(object):
    def maxPathSum(self, root):
        res = [float("-inf")]

        def DFS(node):
            if not node:
                return 0

            # 추가한 건 여기서 0보다 작은 경우에는 그걸 total에 포함시키지 않았다는 것.
            left = max(DFS(node.left),0)
            right = max(DFS(node.right),0)
            total = node.val + left + right
            res[0] = max(res[0], total)

            # 근데 이 부분은 왜 그런거지? 왜 left+right가 아니라, max(left,right)를 리턴하는 거지?
            # 이유는, left+right가 아닌 max(left,right)를 리턴하는 이유는,

            # 근데 둘다 양수인 경우에는, left+right가 더 크다. 그럼 왜 max를 리턴하는 거지?
            # 그 이유는, 내 생각에는, 
            # 여기서 return 하는 것은 비교를 위한 값이다.
            # 그 말인 즉슨, 그 위에서 봤을때, 한쪽으로만 갈 수 있다는 것이다.

            # 그래서 max(left, right)를 리턴하는 것이다.

            return max(left,right)+node.val

        DFS(root)

        return res[0]
    
    
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def findMaxPathSum(node):
            nonlocal maxi
            if not node:
                return 0
            left = max(findMaxPathSum(node.left), 0)
            right = max(findMaxPathSum(node.right), 0)
            maxi = max(maxi, left + right + node.val)
            return max(left, right) + node.val
        
        maxi = float('-inf')
        findMaxPathSum(root)
        return maxi

