# 다른 사람의 풀이 참고.

# 내가 생각했던거랑 비슷하긴 한데, 단순히 평균을 기준으로 하는게 아니라,
# 그 기준 자체를 찾아보는 것이다. mid를 이제 최소치로 두고, 그것을 기준으로.


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        # Edge case: When there's no splits required at all
        if k == 1:
            return sum(nums)

        # logic 
        left, right = max(nums), sum(nums)
        while left <= right :
            mid = ( left + right ) // 2
            summ = 0
            splits = 1
            for i in nums:
                summ += i
                if summ <= mid:
                    continue
                else:
                    splits += 1
                    summ = i
            
            # no. of splits exceeds the required splits
            if splits > k:
                left = mid + 1
            
            # if no. of splits are equal or lower than required splits
            # This case is also applicable in 'splits == k', because ???? (refer the pinned comment)
            else:
                right = mid - 1
        
        return left