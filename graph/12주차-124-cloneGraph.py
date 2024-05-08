#4:24. 어디서 해맸냐면. 원본을 stack에 넣어야지, 복사한걸 넣으면 안된다는 이야기이다.

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None

        cloned = {}
        stack = [node]
        cloned[node.val] = Node(node.val,[])

        while stack:
            curr = stack.pop()
            for nv in curr.neighbors:
                if nv.val not in cloned:
                    cloned[nv.val] = Node(nv.val,[])
                    stack.append(nv)

                # 일단 그 친구의 neighbor는 다 넣어줘야 한다.
                cloned[curr.val].neighbors.append(cloned[nv.val])
        
        return cloned[node.val]
    

