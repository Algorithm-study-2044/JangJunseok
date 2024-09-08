# 모르겠다.. 다른 사람의 풀이 참고.

import heapq

class Solution:
    def modifiedGraphEdges(self, n, edges, source, destination, target):
        adjs = [{} for _ in range(n)]

        for edge in edges:
            adjs[edge[0]][edge[1]] = edge[2]
            adjs[edge[1]][edge[0]] = edge[2]

        # source부터 각 노드까지의 거리를 저장하는 리스트
        distTo = [float('inf')] * n
        distTo[source] = 0

        pq = [(0, source)]
        heapq.heapify(pq)

        self.dijkstra(adjs, distTo, pq)

        # 한번 다익스트라 돌렸더니 이미 target과 같다? 그러면 양수값 간선만으로도 갈 수 있다.
        # 그러므로 -1을 따로 고칠 필요 없이, 그냥 양수 최대값으로 만들면 된다.
        if distTo[destination] == target:
            return self.fill(edges)
        # 만약 양수 간선 연결값이 target보다 작다면? 
        elif distTo[destination] < target:
            return []

        for edge in edges:
            if edge[2] == -1:
                edge[2] = 1
                adjs[edge[0]][edge[1]] = 1
                adjs[edge[1]][edge[0]] = 1

                pq = [(distTo[edge[0]], edge[0]), (distTo[edge[1]], edge[1])]

                self.dijkstra(adjs, distTo, pq)

                if distTo[destination] == target:
                    return self.fill(edges)
                elif distTo[destination] < target:
                    edge[2] += target - distTo[destination]
                    adjs[edge[0]][edge[1]] = edge[2]
                    adjs[edge[1]][edge[0]] = edge[2]
                    return self.fill(edges)

        return []

    def fill(self, edges):
        for edge in edges:
            if edge[2] == -1:
                edge[2] = int(2e9)
        return edges

    # dijkstra 알고리즘을 통해서, source로부터 각 지점까지의 최단거리를 업데이트해준다.
    def dijkstra(self, adjs, distTo, pq):
        while pq:
            _, curr = heapq.heappop(pq)

            for next_node, weight in adjs[curr].items():
                if weight > 0:
                    if distTo[next_node] > distTo[curr] + weight:
                        distTo[next_node] = distTo[curr] + weight
                        heapq.heappush(pq, (distTo[next_node], next_node))

        

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        adjs = [{} for _ in range(n)]

        distTo = [float("inf")] * n
        distTo[source] = 0

        pq = [(0,source)]
        heapify(pq)

        for start,end,weight in edges:
            adjs[start][end] = weight
            adjs[end][start] = weight

        def daikstra(self, adjs, distTo, pg):
            while pq:
                _, curr = heap.heappop(pg)
                
                for next_node, weight in adjs[curr].items():
                    if distTo[next_node] > distTo[curr] + weight:
                        distTo[next_node] = distTo[curr] + weight
                        heapq.heappush(pq,(distTo[next_node],next_node))