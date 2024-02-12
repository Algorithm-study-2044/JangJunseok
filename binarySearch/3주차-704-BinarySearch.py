# 3주차. 2분소요. 그냥 이진탐색문제.

class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1