# 3주차. pass. 198ms. 13% beats. 다시풀것.
class Solution(object):
    def findMode(self, root):
        t1 = [0] * (200001)
        
        def DFS(node):
            if not node:
                return
            t1[node.val+100000] += 1
            DFS(node.left)
            DFS(node.right)
        
        DFS(root)
        maxVal = max(t1)
        result = []

        for index, val in enumerate(t1):
            if val == maxVal:
                result.append(index-100000)
        
        return result
    


#다른 사람의 풀이
    
class Solution(object):
    def __init__(self):
        self.dict = {}
        self.ans=[]
        self.mx=-1
    def solve (self,root):
        if root is None: return
        self.dict[root.val] = self.dict.get(root.val, 0) + 1
        if self.dict[root.val]==self.mx:
            self.ans.append(root.val)
        elif self.dict[root.val]>self.mx:
            self.mx=self.dict[root.val]
            self.ans=[]
            self.ans.append(root.val)

        self.solve(root.left)
        self.solve(root.right)
    def findMode(self, root):
        
        self.solve(root)
        return self.ans