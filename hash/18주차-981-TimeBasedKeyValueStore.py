# 1차시도 성공. 12분 소요. 524ms. 90.11% beats.

# 그냥 defaultdict랑 heap으로 구현하면 안되나?
# 글면 문제는, timestamp보다 작아야 한다는 것.
# 그걸 위해서, 뽑고 temp에 저장해둔다음에 나중에 다시 heappush하는.

# 이건 시간복잡도 NlogN이다.

import heapq
class TimeMap:

    def __init__(self):
        self.arr = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        # 근데 궁금한건 이렇게 하면 최초 list가 힙인지? 힙이다. 
        # 여기에 하나를 넣어도 그건 힙이다. 그리고 그 다음부터는 heappush하니까 힙이다.
        heap = self.arr[key]
        heapq.heappush(heap,(-timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.arr:
            return ""
        temp = []
        while self.arr[key] and -self.arr[key][0][0] > timestamp:
            temp.append(heapq.heappop(self.arr[key]))
        
        if self.arr[key]:
            ans = self.arr[key][0][1]
        else:
            ans = ""

        for t in temp:
            heapq.heappush(self.arr[key],t)

        return ans
    

# 다른 사람의 풀이. binary search로 풀었다.
# logN으로 줄어든다.

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        data = self.store.get(key, [])
        low = 0
        high = len(data) - 1
        ans = ""

        while low <= high:
            mid = low + (high - low) // 2
            if data[mid][1] <= timestamp:
                ans = data[mid][0]
                low = mid + 1
            else:
                high = mid - 1
            
        return ans

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

