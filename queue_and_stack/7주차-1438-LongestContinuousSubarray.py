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
            #maxQueue에는 현재까지의 최대값만 저장한다. 그렇다고 해서 현제값까지의 최대를 다 저장하는 힙같은건 또 아니다.
            #그럼 도대체 뭐가 저장되는거지? 최대 있을때, 그 오른쪽에 있는 얘들 중에서 그 다음으로 큰 애가 저장된다.
            #그렇게 하면 sliding window시에 최대값을 업데이트하면서. 조건에 맞는지를 계속 비교해볼 수 있다.
            while maxQueue and maxQueue[-1] < num:
                maxQueue.pop()
            
            maxQueue.append(num)
            
            while minQueue and minQueue[-1] > num:
                minQueue.pop()
                
            minQueue.append(num)

# sliding window의 시작지점과 끝지점을 이야기하는것 같음.
# 일단 max-min이 limit보다 크면? 무조건 시작지점을 옮긴다. 
# 그 과정에서 최대 최소값도 갱신해주고. 아마 그 과정을 이야기하는것 같다.
            
# 왜 queue를 쓰는가? 그것은. sliding window에서 기존 max, min값이 있을때, 그게 안되면 갱신해주는데, 그 갱신해주었을때의
# 새로운 최대, 최소를 찾아주기 위함인듯하다. 
            
            while maxQueue[0] - minQueue[0] > limit:
                
                if maxQueue[0] == nums[i]:
                    maxQueue.popleft()
                if minQueue[0] == nums[i]:
                    minQueue.popleft()
                
                i += 1
            maxSize = max(maxSize, j - i + 1)
        return maxSize