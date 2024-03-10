# 1차시도. 시간초과 실패. [1,1,1,1,1,1,1,1,1,1,1,1,1,1] limit = 10일때. 
# 근데 그러면 else문에서 end += 1만 하는건데 왜 시간복잡도가 늘어나는걸까?

class Solution(object):
    def longestSubarray(self, nums, limit):

        arr = []
        start = 0
        end = 1
        maxLen = 1
        while start <= len(nums) - 1 and end <= len(nums):
            curr = nums[start:end]
            if max(curr) - min(curr) > limit:
                start += 1
                end = start + 1
                maxLen = max(maxLen,len(curr)-1)
            else:
                end += 1
                maxLen = max(maxLen,len(curr))

# 그러니까. 현재 array에서 min과 max를 찾아서 그 차이가 limit보다 작으면 end를 늘리고, 그 차이가 limit보다 크면 start를 늘리는 방식으로 풀어야 한다.
# 그런데 이렇게 하면 시간복잡도가 O(n^2)가 되어버린다. 그래서 이걸 줄이기 위해 deque를 사용한다.
# deque를 사용하면 O(1)의 시간복잡도로 min과 max를 찾을 수 있다.

# 2차시도. 다른 사람의 풀이 연구.
                
# 내가 궁금한건. min, max값을 기록하기 위해서라면 그냥 min = 0 max = 0 이런식으로 값만 쓰면 안되나?

# 16, 8 ,4 가 있을때 10이 들어가면, 16, 10 이렇게 maxQue에 남는다.                

from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxQueue = deque()
        minQueue = deque()
        
        length = len(nums)
        
        i = 0
        maxSize = 0
        
        for j, num in enumerate(nums):
            while maxQueue and maxQueue[-1] < num:
                maxQueue.pop()
            
            maxQueue.append(num)
            
            while minQueue and minQueue[-1] > num:
                minQueue.pop()
                
            minQueue.append(num)
            
            while maxQueue[0] - minQueue[0] > limit:
                if maxQueue[0] == nums[i]:
                    maxQueue.popleft()
                if minQueue[0] == nums[i]:
                    minQueue.popleft()
                
                i += 1
            maxSize = max(maxSize, j - i + 1)
        return maxSize