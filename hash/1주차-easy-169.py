# 1차시도. 메모리 초과.
class Solution(object):
    def majorityElement(self, nums):
        arr = [0] * (max(nums)+1)
        for item in nums:
            arr[item] += 1
        
        return arr.index(max(arr))
    
#2차 시도.
class Solution(object):
    def majorityElement(self, nums):
        hash = {}
        for item in nums:
            if item not in hash:
                hash[item] = 0
            else:
                hash[item] += 1
        
        return sorted([item for item in hash.items()],key=lambda x:-x[1])[0][0]