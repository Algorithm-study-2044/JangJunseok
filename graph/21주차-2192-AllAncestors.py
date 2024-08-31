# 문제: 2192. All Ancestors

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        direct_child = [[] for _ in range(n)]
        ans = [[] for _ in range(n)]
        for e in edges:
            direct_child[e[0]].append(e[1])
        for i in range(n):
            self.DFS(i,i,direct_child,ans)
        return ans
        
    def DFS(self,top_parent,current,direct_child,ans):
        for child in direct_child[current]:
            if not ans[child] or ans[child][-1] != top_parent:
                ans[child].append(top_parent)
                self.DFS(top_parent,child,direct_child,ans)