#[1,2,3,null,null,4,5,6,7] 에서 막혔는데.
#왜 그런가 하면. serialize 과정에서, 동일하게 t를 채워넣었어야 했는데, 그렇게 하지 않았기 때문이다.
#그렇지 않으면 결국 순서가 안맞을 수밖에 없다.

class Codec:
    def serialize(self, root):
        queue = deque([root])
        arr = []
        while queue:
            curr = queue.popleft()
            if curr:
                print(curr.val)
            if curr:
                arr.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                arr.append("t")
        res = ",".join(arr)
        return res
        
    def deserialize(self, data):
        def DFS(idx,parent,isLeft,ser):
            if idx > len(ser) -1 or ser[idx] == "t":
                return

            target = TreeNode(int(ser[idx]))
            if parent:
                if isLeft:
                    parent.left = target
                else:
                    parent.right = target
            
            left = idx * 2 + 1
            right = idx * 2 + 2

            DFS(left,target,True,ser)
            DFS(right,target,False,ser)

            return target
        ser = data.split(",")
        return DFS(0,None,False,ser)