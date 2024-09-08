# 다른 사람의 풀이 참고.
# n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        # 시작점에서의 prob을 다 업데이트해준다.
        dist = [0] * n
        # start_node에서의 prob은 1이다.
        dist[start_node] = 1

        for _ in range(n-1):
            updated = False
            for i, (u,v) in enumerate(edges):   
                # 두 지점을 연결하는 간선을 테스트
                if succProb[i] * dist[u] > dist[v]:
                    dist[v] = succProb[i] * dist[u]
                    updated = True
                if succProb[i] * dist[v] > dist[u]:
                    dist[u] = succProb[i] * dist[v]
                    updated = True
            if not updated:
                return dist[end_node]

        return dist[end_node]
    

# 벨만-포드 알고리즘.

# 다익스트라

# 시작점에서 출발 -> 거리 업데이트 -> 그로 인해서 그 지점에서 출발하는 어떤 지점들의 거리도 다시 계산해야 함.
# -> 그 지점을 큐에 넣음. -> 큐에 넣은 지점으로 이동해서, 그 부분의 거리를 다시 계산.
# -> 그로 인해 업데이트되는 부분을 계산

