# 26분 소요. 1299ms. 41.38% beats.
# hard문제. 67.3% 짜리 문제이긴 함. ㄱ

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        dependencies = defaultdict(list)
        cost = {}

        for src,target in relations:
            dependencies[target].append(src)

        def get_cost(course):
            if course in cost:
                return cost[course]
            cst = 0
            for child in dependencies[course]:
                cst = max(cst, get_cost(child))
            cst += time[course-1]
            cost[course] = cst
            return cst
        
        return max([get_cost(course) for course in range(1,n+1)])