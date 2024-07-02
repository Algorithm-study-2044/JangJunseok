# 1차시도. 성공. 605ms. 66.63%
# 다른 풀이도 참고해볼것.

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dp = []
        for i in range(len(nums)):
            curr = nums[i]
            if curr % 2 == 1:
                if dp:
                    dp[-1][2] = i
                    dp.append([dp[-1][1],i,None])
                else:
                    dp.append([-1,i,None])
        if dp:
            dp[-1][2] = len(nums)
        res = 0
        for i in range(len(dp)-k+1):
            start = dp[i]
            end = dp[i+k-1]
            res += (start[1]-start[0]) * (end[2]-end[1])

        return res
    
# 다른 사람의 풀이.

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        result, cur, l, cur_sub = 0, 0, 0, 0
        for r, v in enumerate(nums):
            if v % 2 == 1: 
                cur += 1
                cur_sub = 0

            # 만약에 오른쪽으로 옮겼는데도 여전히 k이다..이러면 cur_sub를 계속 더해주면 된다.
            while cur == k:
                if nums[l] % 2 == 1:
                    cur -= 1
                l += 1
                cur_sub += 1
            result += cur_sub

        return result