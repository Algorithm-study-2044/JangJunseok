class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        flightrecords = {}
        for flight in flights:
            if flight[0] not in flightrecords:
                flightrecords[flight[0]]={flight[1]:flight[2]}
            else:
                flightrecords[flight[0]][flight[1]]=flight[2]
            
        shortestdist = {}
        minHeap = []
        heapq.heappush(minHeap,(0,(src,0)))

        while minHeap and len(shortestdist)!=n:
            weight,node = heapq.heappop(minHeap)
            if node[0] in shortestdist :
                if node[1]<shortestdist[node[0]]:
                    shortestdist[node[0]]=node[1]
                else:
                    continue
            else:
                shortestdist[node[0]] = node[1] 
            
            if node[0]==dst:
                return weight


            if flightrecords.get(node[0]):
                for no,we in flightrecords[node[0]].items():
                    if n not in shortestdist and (node[1]<k or no==dst):
                        heapq.heappush(minHeap,(weight+we,(no,node[1]+1)))

        return -1


# 3차시도. 시간초과 실패.    

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for start,end,cost in flights:
            graph[start][end] = cost
        
        min_val = [float("inf")]

        def travel(curr,cost,cnt,seen,min_val):            
            if cost >= min_val[0] or cnt > k+1:
                return -1

            if curr == dst and cnt <= k+1:
                min_val[0] = min(min_val[0],cost)
                return cost
            
            for neigh,val in graph[curr].items():
                if neigh not in seen:
                    seen.add(neigh)
                    travel(neigh,cost+val,cnt+1,seen,min_val)
                    seen.remove(neigh)

        travel(src,0,0,set(),min_val)

        if min_val[0] != float("inf"):
            return min_val[0]
        else:
            return -1


# 1차시도. 시간초과 실패.
# 그러면 그냥 dfs로, 0에서 travel하면? 

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(dict)
        for start,end,cost in flights:
            graph[start][end] = cost
        
        def travel(curr,cost,cnt,seen):
            if curr == dst and cnt <= k+1:
                return cost
            
            min_val = float("inf")

            for neigh,val in graph[curr].items():
                if neigh not in seen:
                    seen.add(neigh)
                    result = travel(neigh,cost+val,cnt+1,seen)
                    seen.remove(neigh)
                    if result != -1:
                        min_val = min(min_val, result)

            if min_val != float("inf"):
                return min_val
            else:
                return -1

        return travel(src,0,0,set())

# 2차시도. 이번에는 백트래킹을 넣어봤는데, 여전히 실패함.
# 이렇게 했는데 틀린 답이라고 하네.
# 아 그건 안의 루프에서 result중에 가장 작은 값을 가져가야 하는데,
# 그런데 지금 min_val이라는걸 백트래킹으로 했는데.

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for start,end,cost in flights:
            graph[start][end] = cost
        
        min_val = [float("inf")]
        
        def travel(curr,cost,cnt,seen,min_val):            
            if cost >= min_val[0]:
                return -1

            if curr == dst and cnt <= k+1:
                return cost
            
            min_local = float("inf")
            for neigh,val in graph[curr].items():
                if neigh not in seen:
                    seen.add(neigh)
                    result = travel(neigh,cost+val,cnt+1,seen,min_val)
                    seen.remove(neigh)
                    if result != -1:
                        min_local = min(min_local,result)

            if min_local != float("inf"):
                return min_local
            return -1

        min_val[0] = min(min_val[0],travel(src,0,0,set(),min_val))

        if min_val[0] != float("inf"):
            return min_val[0]
        else:
            return -1