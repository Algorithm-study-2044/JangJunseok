#3주차. 1차시도 시간초과 실패. 근데 이거 DFS로 풀어야 하는ㄱㅔ 맞는거 아닌가? 왜 BFS로 풀어야 하는거지?

class Solution(object):

    def checkSymm(arr):
        flag = True
        for i in range(len(arr)//2):
            if arr[i] != arr[-i-1]:
                flag = False
        return flag

    def isSymmetric(self, root):
        flag = True
        allArr = []
        def BFS(node):
            queue = [node]
            while queue:
                newNode = queue.pop(0)
                if not newNode:
                    allArr.append(None)
                else: 
                    allArr.append(newNode.val)
                    if newNode.left:
                        queue.append(newNode.left)
                    if newNode.right:
                        queue.append(newNode.right)
        
        BFS(root)
        flag = True
        
        for i in range(n):
            flag = self.checkSymm(allArr[2**i-1:2**i-1+2**i])
            if not flag:
                return flag
        
        return flag
        