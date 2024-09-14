# 11:15 시작. 60ms. 76.23% beats.
# 뭔가 풀긴 풀었는데 관련해서 예외처리를 너무 많이 한 느낌이다.

# 이 문제가 하향식으로 풀어야 하는 핵심이라고 생각함.
# 재귀를 통해서.

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float("-inf")]
        minus = [float("-inf")]

        def travel(node):
            if not node:
                return 0
            if node.val <= 0:
                minus[0] = max(minus[0],node.val)

            center = node.val
            left = travel(node.left)
            right = travel(node.right)
            res[0] = max(res[0],left+center+right,0)

            return max(left+center,right+center,0)

        result = travel(root)
        final = max(res[0],result)
        if final == 0 and minus[0] != float("-inf"):
            return minus[0]
        return final
    

# 다른 사람의 풀이 참고.
# 비슷하게는 접근했는데 말이지.

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        ans = -inf
        
        def check(node):

            nonlocal ans

            if not node:
                return 0
            
            l = max(0, check(node.left))
            r = max(0, check(node.right))

            ans = max(ans, l + node.val + r)

            return node.val + max(l, r)
        

        check(root)
        return ans
    

# 참고한 나의 풀이 수정.

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float("-inf")]

        def travel(node):
            if not node:
                return 0

            center = node.val
            left = max(travel(node.left),0)
            right = max(travel(node.right),0)
            res[0] = max(res[0],left+center+right)

            return max(left+center,right+center)

        result = travel(root)
        return max(res[0],result)