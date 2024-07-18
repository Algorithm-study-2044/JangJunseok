# 2:38. 1차시도. 시간초과.


# 정답 풀이.
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        q: list[TreeNode] = [root]
        while q:
            cur_node: TreeNode = q.pop()
            if cur_node.val == startValue:
                start_node = cur_node  # here we're setting up the start node
                break

            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)

        # child node value -> TreeNode object which is parent to node with this value
        nodes_parents: dict[int, TreeNode] = {}
        q = [root]
        while q:
            cur_node = q.pop()
            if cur_node.left:
                nodes_parents[cur_node.left.val] = cur_node
                q.append(cur_node.left)
            if cur_node.right:
                nodes_parents[cur_node.right.val] = cur_node
                q.append(cur_node.right)

        visited = set()
        q = [start_node]
        # key is the destination node to which we travel - value is a tuple with 2 elements - (source_node, direction)
        tracked_path: dict[TreeNode, tuple(TreeNode, str)] = {}

        while q:
            cur_node = q.pop()
            visited.add(cur_node)

            if cur_node.val == destValue:
                destination_node = cur_node
                break  # we've reached the target node

            if cur_node.val in nodes_parents and nodes_parents[cur_node.val] not in visited:
                parent = nodes_parents[cur_node.val]
                q.append(parent)
                tracked_path[parent] = (cur_node, "U")  # this is parent node, we go up

            if cur_node.left and cur_node.left not in visited:
                q.append(cur_node.left)
                tracked_path[cur_node.left] = (cur_node, "L")

            if cur_node.right and cur_node.right not in visited:
                q.append(cur_node.right)
                tracked_path[cur_node.right] = (cur_node, "R")

        # Now we need to construct path in a string from tracked_path we have
        result_path: list[str] = []
        cur_node = destination_node

        while cur_node != start_node:
            source_node, direction = tracked_path[cur_node]
            result_path.append(direction)  # directions will be in reversed order
            cur_node = source_node

        result_path.reverse()
        return "".join(result_path)


# 두 노드의 최소 공통 부모를 찾는다.
# 그게 있다? 그러면 이제 두개를 합쳐야 함.
# DFS([].append("L"))

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        res[0] = [""]
        def DFS(node,path):
            if not node:
                return
            left = DFS(node.left,"L")
            right = DFS(node.right,"R")

            point = None
            if node.val == startValue
                point = (0,"")
            elif node.val == destValue
                point = (1,"")
            

            # 끌어올릴때는 내게 주어진 path 1개를 더해서 올려야지.
            if left and right:
                
            elif left and point:
                
                # left 있고 point인 경우.
            elif right and point:
                
            elif left:
                return (left[0],left[1] + path)
            elif right:
                return (right[0],right[1]+ path)
            else:
                return None
                
        
        DFS(root,"")

        return res[0]
    

# 공통 조상을 찾는다.
# 그리고 이제 start에서 온 경로를 다 U로 바꾼다음
# endValue는 그대로 합쳐준다.

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        res = ""
        def DFS(node,accum):
            if not node:
                return ""
            flag = None
            if node.val == startValue:
                flag = (1,"")
            elif node.val == destValue:
                flag = (2,"")

            lv = DFS(node.left,"L") # (isStart,)
            rv = DFS(node.right,"R")

            if (flag and lv) or (flag and rv):
                if flag[0] == 1:
                    if lv:
                        res = lv[1]
                    else:
                        res = rv[1]
                else:
                    if lv:
                        res += "U" * len(lv[1])
                    else:
                        res += "U" * len(rv[1])
                    
            elif lv and rv:
            
            else:

