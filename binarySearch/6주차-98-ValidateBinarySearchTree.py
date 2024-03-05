# 4:00  validate bineary search tree
# 이렇게 하면 근데,
# [5,4,6,null,null,3,7] 의 예에서, 3을 걸러낼 수 있나?
# 3의 경우에는 1루트의 오른쪽, 2루트의 왼쪽인데.

class Solution(object):
    def isValidBST(self, root):
        return self.checkValidandSmall(root.left,[root.val]) and self.checkValidandBig(root.right,[root.val])


    def checkValidandSmall(self,node,parents):
        if not node:
            return True
        
        if all([node.val < item for item in parents]) and self.checkValidandSmall(node.left, parents.append(node.val)) and self.checkValidandBig(node.right,parents.append(node.val)):
            return True
        else:
            return False
    
    def checkValidandBig(self,node,parents):
        if not node:
            return True
        
        if all([node.val > item for item in parents]) and self.checkValidandSmall(node.left, parents.append(node.val)) and self.checkValidandBig(node.right,parents.append(node.val)):
            return True
        else:
            return False
        

#2차시도. 시간초과 실패.
        
class Solution(object):
    def isValidBST(self, root):
        
        def DFS(node):
            if not node:
                return [None]

            all_values = []

            from_left = DFS(node.left)
            from_right = DFS(node.right)
            if not from_left or not from_right:
                return False
            
            if not from_left or not all([node.val > item for item in from_left]) or not from_right or not all([node.val > item for item in from_right]):
                return False
    
            all_values.extend(from_left)
            all_values.extend(from_right)
            all_values.append(node.val)

            return all_values

        print(DFS(root.left),all([root.val > item for item in DFS(root.left)]))
        print(DFS(root.right),all([root.val < item for item in DFS(root.right)]))
    
        return DFS(root.left) and all([root.val > item for item in DFS(root.left)]) and DFS(root.right) and all([root.val < item for item in DFS(root.right)])
    

#3차시도. 다른사람의 풀이 연구.