#3주차. 근데 이게 왜 binarySearch인거지?
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        return (n * (n + 1)) // 2 - sum(nums)
    

    
        