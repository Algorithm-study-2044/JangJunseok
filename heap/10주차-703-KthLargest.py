# 3:01 -> 3:17분. 16분 소요. 73ms. 87.75% beats.

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        lt = len(nums)
        if lt <= k:
            self.nums = sorted(nums)
        else:
            self.nums = sorted(nums)[lt-k:lt]

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums,val)
        
        else:
            #만약 들어오는 애가, 현재 target보다 작거나 같으면 변동없음.
            if self.nums and self.nums[0] >= val:
                pass
            else:
                heapq.heappop(self.nums)
                heapq.heappush(self.nums,val)
        
        return self.nums[0]
    

# 다른 사람의 풀이 연구. 비슷함.
# k번째까지 하기 위해서 len과 while문을 사용할 수도 있다.
    
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Initialize min-heap with the first k elements
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        # Keep only the k largest elements
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Add new element to the min-heap
        heapq.heappush(self.minHeap, val)
        # If heap size exceeds k, remove the smallest element
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        # Return the current kth largest element
        return self.minHeap[0]