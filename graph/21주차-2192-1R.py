# 6:35 시작. 626ms. 27.57% beats.
# 이런 것들을 이해하는데 필요한 것이라고 한다면..글쎄 그렇게 생각을 하지만.

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        childGraph = defaultdict(list)
        for ed in edges:
            childGraph[ed[0]].append(ed[1])

        ans = [[] for _ in range(n)]

        def DFS(top_parent,current,childGraph,ans):
            for c in childGraph[current]:
                if not ans[c] or ans[c][-1] != top_parent:
                    ans[c].append(top_parent)
                    DFS(top_parent,c,childGraph,ans)

        for i in range(n):
            DFS(i,i,childGraph,ans)

        return ans