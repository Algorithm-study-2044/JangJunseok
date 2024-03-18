#1차시도. 20분. 시간초과 실패.

import heapq

class Solution(object):
    def maxFrequency(self, nums, k):
        gap = []
        nums = sorted(nums)
        freq = Counter(nums)
        for j in range(len(nums)-1):
            heapq.heappush(gap,(nums[j+1]-nums[j],nums[j+1]))
        while gap:
            curr = heapq.heappop(gap)
            if curr[0] > k:
                # 이러면 이제 더 못뺌.  
                return max(freq.values())
            k -= curr[0]
            freq[curr[1]] += 1
            # 이 다음에 heap에 다시 넣어줘야 한다. 이전거랑 똑같아졌으니까.
            heapq.heappush(gap,gap[0])


#2차시도. 풀이 연구. 언제 투포인터를 활용하는가?
#
            
# max frequency -> max length. 만들 수 있는 가장 긴 array를 만들면 된다.
            
class Solution(object):
    def maxFrequency(self, nums, k):
        maxFrequency = 0 
        currentSum = 0  

        nums.sort()  

        left = 0
        for right in range(len(nums)):
            currentSum += nums[right]  

            # 만약에 k를 더한다고 하더라도, nums[right]만 있는 array를 못만들 경우에는, left를 하나 옮겨야 한다.
            while currentSum + k < nums[right] * (right - left + 1):
                currentSum -= nums[left]  # Adjust the subarray sum by removing the leftmost element
                left += 1  # Move the left pointer to the right

            # Update the maximum frequency based on the current subarray length
            maxFrequency = max(maxFrequency, right - left + 1)

        return maxFrequency
    


# 3차시도. 다른사람의 풀이 연구.