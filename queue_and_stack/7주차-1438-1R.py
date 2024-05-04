#1차시도. 접근법은 맞는것같은데. 뭔가 잘못된 것 같다.

# 일단 정답인 풀이와 비교해보자. 나는 지금 다시 계산하는데, 그러지말고 queue를 쓰면은, 
# 최대값을 pop하면 그 다음 최대값이 남는다. 이렇게 하면 되잖아?


from collections import deque
class Solution(object):
    def longestSubarray(self, nums, limit):
        n = len(nums)
        l=r=maxlen=0
        maxq, minq = deque(), deque()

        while r < n:
            while maxq and nums[maxq[-1]] < nums[r]:
                maxq.pop()
            # 만약 왼쪽이 늘어서 오른쪽은 변함없는데 오른쪽을 
            if not maxq or maxq[-1] != r:
                maxq.append(r)
            
            while minq and nums[minq[-1]] > nums[r]:
                minq.pop()
            if not minq or minq[-1] != r:
                minq.append(r)

            #왜 deque을 쓰는지 여기서 알게된다.
            #그리고 왜 빼주는지.

            # 예를 들어 이전 step에서 left가 +1 이동했는데, 걔가 minq면 안되잖아.
            # 근데 maxq는 그럴 필요 있나? 있따. left+1 햇는데 걔가 maxq였으면,걔도 빼야지.
            if minq[0] < l:
                minq.popleft()
            if maxq[0] < l:
                maxq.popleft()

            
            diff = nums[maxq[0]] - nums[minq[0]]
            
            if diff > limit:
                # 이러면 왼쪽이 줄어야 함.
                l += 1
            else:
                # 아니면 계산하고, 다음으로 넘어감.
                maxlen = max(maxlen,r-l+1)
                r += 1
        
        return maxlen



# 일단 반복문을 돌릴때는. 

# sliding window를 활용할때는.

# 작업 1에서는 minq를 만든다. 현재 가지고 있는 것들로부터. 그래서 minq에는 현재까지의 최소값들이 들어간다.

# 궁금한 것은, 왼쪽을 줄였을때, minq에도 줄여줘야할텐데, 그걸 안해도 되는 이유는 뭘까?
# 왼쪽을 줄였을때, minq에도 줄여줘야할텐데, 그걸 안해도 되는 이유는 뭘까?
# 그 이유는, 지금 밑에서, i가 minq[0]보다 작으면, minq[0]을 pop해주기 때문이다.



class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        i = j = maxlen = 0
        
        # minq is a monotonically increasing queue
        # maxq is a monotonically decreasing queue
        # both queue store indices of the values
        minq, maxq = deque(), deque()
        maxlen = 0
        while j < n:
            # preserve the monotonicity of the minq
            while minq and nums[minq[-1]] > nums[j]:
                minq.pop()
            # NOTE: check if the index we are pushing is not already pushed
            if not minq or minq[-1] != j:
                minq.append(j)
            
            # preserve the monotonicity of the maxq
            while maxq and nums[maxq[-1]] < nums[j]:
                maxq.pop()
            # NOTE: ensure we don't push duplicate indices
            if not maxq or maxq[-1] != j:
                maxq.append(j)
            
            # ensure minq and maxq don't have elements out of range of [i, j]
            if i > minq[0]:
                minq.popleft()
            if i > maxq[0]:
                maxq.popleft()
            
            # update maxlen and increment i and j
            minval = nums[minq[0]]
            maxval = nums[maxq[0]]
            if maxval - minval <= limit:
			    # if the window is valid we move j to right
                maxlen = max(maxlen, j - i + 1)
                j += 1
            else:
			    # otherwise we shrink the window by moving i to the right
                i += 1
        
        return maxlen
    


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
                
                # 왼쪽으로 축소는 기정사실인데, 만약 축소하는 애가 min이나 max이면, 그 값을 업데이트해주어야 하는거다.
                if maxQueue[0] == nums[i]:
                    maxQueue.popleft()
                if minQueue[0] == nums[i]:
                    minQueue.popleft()
                
                i += 1
            maxSize = max(maxSize, j - i + 1)
        return maxSize
    


from collections import deque
class Solution(object):
    def longestSubarray(self, nums, limit):
        n = len(nums)
        l=r=maxlen=0
        maxq, minq = deque(), deque()

        while r < n:
            while maxq and nums[maxq[-1]] < nums[r]:
                maxq.pop()
            # 만약 왼쪽이 늘어서 오른쪽은 변함없는데 오른쪽을 
            if not maxq or maxq[-1] != nums[r]:
                maxq.append(r)
            
            while minq and nums[minq[-1]] > nums[r]:
                minq.pop()
            if not minq or minq[-1] != r:
                minq.append(r)

            #왜 deque을 쓰는지 여기서 알게된다.
            #그리고 왜 빼주는지.

            # 예를 들어 이전 step에서 left가 +1 이동했는데, 걔가 minq면 안되잖아.
            # 근데 maxq는 그럴 필요 있나? 있따. left+1 햇는데 걔가 maxq였으면,걔도 빼야지.
            if minq[0] < l:
                minq.popleft()
            if maxq[0] < l:
                maxq.popleft()

            print(maxq,minq)
            
            diff = nums[maxq[0]] - nums[minq[0]]
            
            if diff > limit:
                # 이러면 왼쪽이 줄어야 함.
                l += 1
            else:
                # 아니면 계산하고, 다음으로 넘어감.
                maxlen = max(maxlen,r-l+1)
                r += 1
        
        return maxlen