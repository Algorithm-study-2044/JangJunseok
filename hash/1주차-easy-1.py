#1차시도. 시간복잡도 O(n^2)이라서 통과는 했지만, 더 효율적인 방법이 있을 것 같다.
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            findVal = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == findVal:
                    return [i,j]
                

#2차 시도.
class Solution(object):
    def twoSum(self, nums, target):
        #nums는 [2,7,11,15]와 같은 리스트
        #target은 9와 같은 정수
        hash_table = {}

        for index, value in enumerate(nums):
            if target-value in hash_table and index != hash_table[target-value]:
                return [index,hash_table[target-value]]
