#4주차. 820ms. 52% beats. sorting 없이.

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):

        self.li = []
        for i in nums:
            heapq.heappush(self.li,[-i,i])
        for _ in range(k-1):
            heapq.heappop(self.li)
        return heapq.heappop(self.li)[1]