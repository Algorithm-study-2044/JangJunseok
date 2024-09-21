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
    
    # topdown으로, 0에서 자식들을 타고 내려가면서, top_parent들을 자식의 ans에 추가해준다.
    def DFS(self,top_parent,current,direct_child,ans):
        for child in direct_child[current]:
            # 여기서 없으면 그냥 추가가능. 누가 있으면? 어차피 0은 0대로, 1은 1대로. 이렇게 처리가 되기 때문에 순서대로 되겠지만,
            # 0이 두번쌓이는 경우가 있을 수 있다. 왜? 만약에 
            if not ans[child] or ans[child][-1] != top_parent:
                ans[child].append(top_parent)
                self.DFS(top_parent,child,direct_child,ans)