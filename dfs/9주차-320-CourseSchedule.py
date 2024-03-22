# 1차시도. 10분 소요. 87ms. 77% beats.

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:       
        res = []
        visited = 0
        graph = defaultdict(list)
        pre_cnt = [0] * numCourses
    
        for pre in prerequisites:
            pre_cnt[pre[0]] += 1
            graph[pre[1]].append(pre[0])

        initial_queue = [index for index,value in enumerate(pre_cnt) if value == 0]

        def DFS(num):   
            nonlocal visited
            res.append(num)
            visited += 1
            for target in graph[num]:
                pre_cnt[target] -= 1
                if pre_cnt[target] == 0:
                    DFS(target)


        for course in initial_queue:
            DFS(course)

        if visited == numCourses:
            return res
        else:
            return []