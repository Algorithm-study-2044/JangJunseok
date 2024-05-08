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
    

# 그러면 해야할것은, 한번 DFS를 해서, 기댓값을 계산한다음에,
# 그 다음에 root부터 내려가면서, 그걸 선택할지 안할건지를.

# 근데 노드가 있을때, 노드를 먹을건지, 아니면 노드먹고 왼쪽을 먹을건지, 노드먹고 오른쪽을 먹을건지.
# 문제는 노드를 먹을건지 판단하는 과정이, 아니 애초에 rootNode 부터 시작하지 않을수도 있다는게 문제이다.

# 아니 루트에서 시작해서, 해당 루트가 그만큼의 가치가 없으면 버리고.
# 