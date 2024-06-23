# 11:27. 실패.

from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_q = deque([])
        min_q = deque([])
        max_len = 0

        for i in range(len(nums)):
            curr = nums[i]

            while max_q and nums[max_q[-1]] < curr:
                max_q.pop()
            max_q.append(i)

            while min_q and nums[min_q[-1]] > curr:
                min_q.pop()
            min_q.append(i)

            if max_q and curr > nums[max_q[0]]:
                # 이러면 이제 min_q값을 계속 꺼내주면서.. 언제까지? limit보다 작을때까지.
                while curr - nums[min_q[0]] > limit:
                    min_q.popleft()

                max_len = max(max_len, i - nums[min_q[0]]+1)
                
            elif min_q and curr < nums[min_q[0]]:
                while nums[max_q[0]] - curr > limit:
                    max_q.popleft()
                
                max_len = max(max_len, i - nums[max_q[0]]+1)
                
        return max_len  