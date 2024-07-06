# 3:40. 1차시도. 시간 초과...

# 그런데 하나의 여정에서, 이미 갔던 버스의 경우에는 재귀하지 않는다.
# -1은 언제? 모든 버스가 다 seen에 있지만, 목적지에 못 갔을때,
# 즉 체크 -> 모두 seen? -> 아니면 그 val 제외하고 다시 재귀.

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
    





        

        