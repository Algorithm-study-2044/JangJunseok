# 3차시도. 20분 소요. 26ms. 56% beats.
# 최소, 최대값을 계속 업데이트해주면서, DFS를 해주면 된다.

class Solution(object):
    def isValidBST(self, root):

        def DFS(node,minVal,maxVal):
            if not node:
                return True

            # 조건을 봐봐. 왼쪽 node가 루트노드보다 같아도 안된다. 커도 안되지만.
            if node.val >= maxVal or node.val <= minVal:
                return False
            
            newMinVal = max(node.val, minVal)
            newMaxVal = min(node.val, maxVal)

            return DFS(node.left,minVal,newMaxVal) and DFS(node.right,newMinVal,maxVal)
        
        return DFS(root,float("-inf"), float("inf"))



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
    

#3차시도. 
    