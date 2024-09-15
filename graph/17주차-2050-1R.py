# 11:17 시작. 21분 소요. 1308ms. 45.82% beats.

# 일단 pre가 0인것들만 모아서, queue에 넣는다.
# 이들은 병렬적으로 처리할 수 있다.

# 5 입장에서는, 가장 큰 그래프 시간을 따라갈 수 밖에.
# 7 + 5 = 12 라는 것이다.

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        graph = defaultdict(list)
        head = set(range(1,n+1))

        for start,end in relations:
            graph[end].append(start)
            if start in head:
                head.remove(start)

        dp = [None] * (n+1)

        def travel(node):
            if dp[node-1]:
                return dp[node-1]
            
            cost = time[node-1]
            max_val = 0

            for dependency in graph[node]:
                max_val = max(max_val,travel(dependency))
            
            dp[node-1] = cost + max_val

            return dp[node-1]

        # 그 다음 루트노드들에 대해서 모두 travel하고 그 값들중에서 max값을 구한다?
        time.append(0)
        for h in head:
            graph[n+1].append(h)
        
        return travel(n+1)