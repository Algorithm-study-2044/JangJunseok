# 9:39 시작.
# 1차시도 실패. 접근 자체는 비슷했는데. 어디서 틀린거지. 접근이 미묘하게 다르다.

# 만약에 해당 노드가 to_delete에 있으면, 
# 그 밑에 있는 자식들은 각각의 숲을 이룰것이고.
# 즉 왼쪽 오른쪽이 to_delete에 해당하지 않으면 각각 넣어주고

# 다시 왼쪽 오른쪽 DFS해준다음에,

# to_delete가 아니다? 그러면 그냥 패스.

# 문제는 밑에서 지워지면 현재 노드도 업데이트 되어야 한다는것.
# 돌겠네, 왜 두번 더하는거지?

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = [root]
        seen = {root.val:root}
        
        def DFS(node):
            if not node:
                return None
            
            lv = DFS(node.left)
            rv = DFS(node.right)

            if node.val in to_delete:
                if node.val in seen:
                    del seen[node.val]
                    # 여기서 res도 없애줬어야지. 그러니까,
                    if res[-1] == node:
                        res.pop()
                if node.left:                    
                    seen[node.left.val] = node.left
                if node.right:
                    seen[node.right.val] = node.right
                return None
            else:
                node.left = lv
                node.right = rv
                return node
            
        DFS(root)
        
        for i in seen.values():
            res.append(i)
            
        return res
        
            
# 정답 풀이.

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: list[int]) -> list[TreeNode]:
        res: dict[int, TreeNode] = {root.val: root}
        to_delete: set[int] = set(to_delete)

        def recursion(parent: TreeNode | None, cur_node: TreeNode | None, isleft: bool) -> None:
            nonlocal res
            if cur_node is None:
                return

            recursion(cur_node, cur_node.left, True)
            recursion(cur_node, cur_node.right, False)

            if cur_node.val in to_delete:
                if cur_node.val in res:
                    del res[cur_node.val]

                if parent:
                    if isleft:
                        parent.left = None
                    else:
                        parent.right = None

                if cur_node.left:
                    res[cur_node.left.val] = cur_node.left
                if cur_node.right:
                    res[cur_node.right.val] = cur_node.right

        recursion(None, root, False)
        return res.values()