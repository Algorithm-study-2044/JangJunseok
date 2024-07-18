# 1차시도. 시간초과 실패.

import heapq
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # food -> type
        self.type_dict = {}
        # type -> ratings
        self.dict = defaultdict(list)
        
        for i in range(len(foods)):
            self.type_dict[foods[i]] = cuisines[i]
            heapq.heappush(self.dict[cuisines[i]],[-ratings[i],foods[i]])

    def changeRating(self, food: str, newRating: int) -> None:
        target_type = self.type_dict[food]
        temp = []
        curr = [None,None]
        while curr[1] != food:
            if curr[1] != None:
                temp.append(curr)
            curr = heapq.heappop(self.dict[target_type])
        curr[0] = -newRating
        temp.append(curr)
        for i in temp:
            heapq.heappush(self.dict[target_type],i)

    def highestRated(self, cuisine: str) -> str:
        return self.dict[cuisine][0][1]
    

from sortedcontainers import SortedSet # f.or better time complexity
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.map1 = defaultdict(SortedSet)  # cuisine -> (rating, food)
        self.map2 = defaultdict(list)  # food -> (cuisine, rating)
        for x, y, z in zip(foods, cuisines, ratings):
            self.map1[y].add((-z, x))
            self.map2[x].append((y, z))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.map2[food][0]
        self.map1[cuisine].remove((-rating, food))
        self.map1[cuisine].add((-newRating, food))
        self.map2[food][0] = (cuisine, newRating)

    def highestRated(self, cuisine: str) -> str:
        return self.map1[cuisine][0][1]