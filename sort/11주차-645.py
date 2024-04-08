# 5:53.

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        flag = False

        nums.sort()

        if len(nums) == 2:
            if nums[0] == 1:
                return [nums[0],nums[1]+1]
            return [nums[0],nums[1]-1]

        res = []
        for i in range(1,len(nums)-2):
            if flag:
                continue

            if not flag and nums[i+1] - nums[i] == 2:
                flag = True
                res.extend([nums[i]-1,nums[i+1]])

            if not flag and nums[i+1] - nums[i] == 0:
                flag = True
                res.extend([nums[i],nums[i+1]+1])
        
        return res