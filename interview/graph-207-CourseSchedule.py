# 10:17 시작.
# 일단 모든 pre를 돌면서, 의존관계를 만든다.
# 0 -> {1}
# 일단 pre_cnt 가 0인 놈들을 queue에 넣는다.
# 그리고 한번 갔던 노드를 다시 갈 필요는 없다.
# queue에서 꺼낸다. 
# 꺼낸 놈을 계속 dfs를 돌면서, pre_cnt를 0으로 만들고,
# 만약 해당 pre_cnt가 0이다? 그러면 그것도 queue에 넣어주고
# 모든 queue가 비었을때 여전히 pre_cnt가 남아있따면 False 아니면 True.

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        pre_cnt = [0] * numCourses
        graph = defaultdict(list)
        seen = set()

        for start,end in prerequisites:
            graph[end].append(start)   
            pre_cnt[start] += 1
        
        def travel(node,pre_cnt,graph):
            if node in seen:
                return
            seen.add(node)
            for neigh in graph[node]:
                pre_cnt[neigh] -= 1
                if pre_cnt[neigh] == 0:
                    travel(neigh,pre_cnt,graph)
        
        for i,val in enumerate(pre_cnt):
            if val == 0:
                travel(i,pre_cnt,graph)
                
        return all([item == 0 for item in pre_cnt])