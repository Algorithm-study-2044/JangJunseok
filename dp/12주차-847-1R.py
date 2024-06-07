class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        queue = deque([(1<<i,i,0) for i in range(n)])
        visited = set((1<<i,i) for i in range(n))

        while queue:
            mask, node, dist = queue.popleft()
            # 이리저리 이동하다 node 노드까지는 온 상태를 기록.

            if mask == (1<<n) - 1:
                return dist

            for next_node in graph[node]:
                new_mask = mask | (1 << next_node)
                # 한번 갔던 경로같은경우에는 다시 가지 않는다.
                if (new_mask, next_node) not in visited:
                    visited.add((new_mask,next_node))
                    queue.append((new_mask,next_node,dist+1))

# 예를 들어 노드가 4개라고 한다면, 모든 노드를 방문한 상황은? 1111이다.
# 즉 그거는 1 << n - 1 이 된다. 

# 0 에서 1 간 상황에서, 다시 0으로 안가나? 

# 다시. 0에서 1갈때. 01,1 이렇게 마스크가 씌워지고
# 1에서 0 갈때, 01,1 이렇게 씌워지고.
# 다시 0에서 1로 가나? ㄴㄴ. 왜? 이제는 visited에 기록되어 있을테니까.

# 그래서 이거는, brute force인건가? 아니, 이거는 bfs

# 비트마스크를 쓰는 이유는, 한번 왔다간 경우에는 다시 갈 필요가 없다는 걸 표현하려고.
# bfs를 쓴 이유는, 각 여정중에서, 가장 빠른 애를 찾아서 return 하면 되기 때문에, bfs를 쓴거다.

