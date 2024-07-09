


# 2차시도. time limit exceeded. 왜?
# 밑에서는 정류장 별로 구했는데, 나는 버스 별로 구했다. 그 점이 다르기는 한데,.

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source == target:
            return 0

        route_dict = defaultdict(list)
        for idx,arr in enumerate(routes):
            for i in arr:
                # 해당 정류장 가는 버스들 저장.
                # ex) 4번 정류장 -> 1번,2번,5번 버스.
                route_dict[i].append(idx)

        def BFS(init):
            queue = deque(init)
            visited = set()
            visited_stops = set()

            while queue:
                bus,cnt = queue.popleft()
                visited.add(bus)
                
                for bus_stop in routes[bus]:
                    if bus_stop in visited_stops:
                        continue

                    visited_stops.add(bus_stop)

                    if bus_stop == target:
                        return cnt

                    for bus_idx in route_dict[bus_stop]:
                    # 아마 이건것같다. 나는 여기서 각 버스를 다시 가고,
                    # 그 버스들에서 다시 정류장을 탐색하는데,

                    # 정답 풀이에서는 정류장 발견하면 바로 return 하니까.
                    # 그래서 더 빠르게 찾는 것 같다.
                        if bus_idx not in visited and cnt < len(routes):
                            queue.append((bus_idx,cnt + 1))
            
            return -1
        
        init = []
        for bus in route_dict[source]:
            init.append((bus,1))
        
        return BFS(init)


# 비슷한데 이건 잘 되었음. 왜?

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source == target:
            return 0

        route_dict = defaultdict(list)
        for idx, arr in enumerate(routes):
            for stop in arr:
                route_dict[stop].append(idx)

        def BFS():
            queue = deque([(source, 0)])  # (current stop, number of buses taken)
            visited_stops = set([source])
            visited_buses = set()

            while queue:
                current_stop, buses_taken = queue.popleft()

                for bus in route_dict[current_stop]:
                    if bus in visited_buses:
                        continue
                    visited_buses.add(bus)

                    for next_stop in routes[bus]:
                        if next_stop == target:
                            return buses_taken + 1
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append((next_stop, buses_taken + 1))

            return -1
        
        return BFS()


# 3:40. 1차시도. memory limit exceeded.

import copy

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source == target:
            return 0

        route_dict = defaultdict(list)
        for idx,arr in enumerate(routes):
            for i in arr:
                route_dict[i].append(idx)

        def BFS(init):
            queue = deque(init)
            while queue:
                bus,gone = queue.popleft()
                for idx,sc in enumerate(routes[bus]):
                    if sc == target:
                        return len(gone)

                # 이미 모든 버스 다 타봤는데도 sc == target이 안나왓다면 가야지.
                    if len(gone) == len(routes) and idx == len(routes[bus])-1:
                        return -1

                    for bus_idx in route_dict[sc]:
                        if bus_idx not in gone:
                            copied_gone = copy.deepcopy(gone)
                            copied_gone.add(bus_idx)
                            queue.append((bus_idx,copied_gone))
            return -1
        
        init = []
        for bus in route_dict[source]:
            gone = set()
            gone.add(bus)
            init.append((bus,gone))
        
        return BFS(init)
    





        

        