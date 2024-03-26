#1차시도. 메모리 초과.

import random

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.arr = []
        for index,item in enumerate(w):
            for _ in range(item):
                self.arr.append((index,item))

    def pickIndex(self):
        idx = random.randrange(0,len(self.arr))
        return self.arr[idx][0]
    

# 2차시도. 다른 사람의 풀이 참고.
    
# 내가 했던 것은. 모든 수를 다 배열에 집어넣는 것이었지만, 이렇게 하면 메모리 초과가 난다.
    
# 그러니까 모든 수를 다 넣지 않고, 누적합을 이용해서
    
# 누적합에서 특정 target이 어느 index에 있는지를 찾아내는 방식으로...
    
class Solution:

    def __init__(self, w: List[int]):
        self.total = sum(w)
        
        pre_sum = [0 for i in range(len(w))]
        for i in range(len(w)):
            if i == 0:
                pre_sum[i] = w[i]
            else:
                pre_sum[i] = w[i] + pre_sum[i - 1]
        # print(pre_sum)
        self.pre_sum = pre_sum
    
    def pickIndex(self) -> int:
		# random.randint(1, 3) includes 1, 2, 3
        pick = random.randint(1, self.total) # or (1, self.pre_sum[-1])
        
        l = 0
        r = len(self.pre_sum) - 1
        while l < r:
            mid = (l + r) // 2
            if pick <= self.pre_sum[mid]:
                r = mid
            else:
                l = mid + 1
                
        # while loop ends when l == r
		# return l is the same as return r
		return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()