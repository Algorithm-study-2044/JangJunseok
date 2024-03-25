# 1차시도. 12분. 23ms. 66% beats.

# python 기본적으로. 함수 안에 함수에서 부모 함수의 변수를 사용하려면 nonlocal을 사용해야 한다.
# 그런데 python1에서는 nonlocal없이, 그냥 print(flag) 하니까 되었다.
# 그런데 이걸 재 할당하는 경우, non-mutable한 boolean을 재할당하면 변수가 메모리에 새로 생성된다.
# 그래서 flag[0] = True로 해야 한다. 그러면 mutable하니까 부모 변수를 제대로 참조한다.
# 여기서 막혀서 조금 시간을 쓴듯.


class Solution(object):
    def hasPathSum(self, root, targetSum):
        flag = [False]

        def DFS(node, curr):
            if not node:
                return

            curr = curr + node.val

            lv = DFS(node.left, curr)
            rv = DFS(node.right, curr)

            if not lv and not rv:
                if curr == targetSum:
                    flag[0] = True
            
            return curr
        
        DFS(root,0)
        return flag[0]