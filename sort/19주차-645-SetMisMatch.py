# 149ms. 87.46% beats. 15분 소요.

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        res = [0,0]
        seen = set()
        for i in nums:
            if i in seen:
                res[0] = i
            seen.add(i)
                
        res[1] = sum([x for x in range(1,len(nums)+1)]) - sum(seen)
        return res
    

