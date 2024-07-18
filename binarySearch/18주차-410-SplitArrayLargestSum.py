# 다른 사람의 풀이 참고.

# 내가 생각했던거랑 비슷하긴 한데, 단순히 평균을 기준으로 하는게 아니라,
# 그 기준 자체를 찾아보는 것이다. mid를 이제 최소치로 두고, 그것을 기준으로.


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        if k == 1:
            return sum(nums)

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
            
            if splits > k:
                left = mid + 1
            
            else:
                right = mid - 1
        
        return left