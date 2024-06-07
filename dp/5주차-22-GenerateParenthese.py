# 1차시도. 성공. 36ms. 67% beats.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def DFS(curr,left,right):
            if left > right:
                return
            
            if len(curr) == n*2:
                res.append(curr)
                return
                
            if left >= 1:
                DFS(curr+"(",left-1,right)
            if right >= 1:
                DFS(curr+")",left,right-1)

        DFS("(",n-1,n)

        return res