#1차시도. 실패. 다른사람의 풀이 참고. bellman ford algorhithm을 사용했다.

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        # create a graph from the flights data
        graph = {}
        for f in flights:
            if f[0] not in graph:
                graph[f[0]] = {}
            graph[f[0]][f[1]] = f[2]

        # n은 도시 개수
        # flights는 [출발도시, 도착도시, 가격]으로 이루어진 리스트
        
        # bellman ford algorithm
        # initialize distance with infinity except src to src which is 0
        distances = [float('inf')] * n
        distances[src] = 0

        for _ in range(k + 1):            
            new_distances = distances[:]

            #k+1번 뭘 해주는가? distance를 업데이트해주는 것이다.
            #왜 k+1번 해주나? 그거는 최대 k+1번 이동할 수 있기 때문이다.
            
            # 모든 도시에 대해서.
            for u in range(n):
                if u in graph:
                    for v in graph[u]:
                        # 모든 길에 대해서 이거를 시행한다.
                        # 그 길의 끝지점으로 가는 거리가, 현재길의 거리 + 그 길의 가격보다 크다면, 업데이트해준다.
                        
                        if distances[u] + graph[u][v] < distances[v]:
                            new_distances[v] = distances[u] + graph[u][v]
            distances = new_distances
        
        return distances[dst] if distances[dst] != float('inf') else -1


#2차시도. BFS로 풀어보기. 
    
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        adj = defaultdict(list)
        visited = [float('inf')] * n
        visited[src] = 0

        # adj의 3에는 , 3번 도시를 출발점으로 하는 도착지와 가격.
        
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))
        
            
        queue = deque([(src, 0)])
        # 근데 여기서 왜 하나를 더해줄까?

        while K >= 0 and queue:
            size = len(queue)
            while size > 0:
                # 현재 queue에 있는것을 다 빼서, visited를 업데이트해준다. 
                # visited는 먼가? 마찬가지로 그 도시까지 가는 비용을 나타낸다.

                curr_node, curr_price = queue.popleft()

                # 현재 노드에서 빼서, 그 이웃도시들까지의 비용을 업데이트해준다. 
                # 결국 visited를 업데이트 해주기 위함.

                for neighbor, price in adj[curr_node]:
                    new_price = curr_price + price
                    if new_price < visited[neighbor]:
                        visited[neighbor] = new_price
                        #왜 다시 queue에 넣어주나? 그 이웃도시를 출발점으로 하는 도착지와 가격을 찾아야 하기 때문이다.
                        queue.append((neighbor, new_price))

                size -= 1
            K -= 1
        
        #두번째 while문 안에서는, queue에 있는것만 다 뺀다. 왜냐하면. 그게 K번째 이동거리에 해당하는 것이기 때문이다.
        

        return visited[dst] if visited[dst] != float('inf') else -1