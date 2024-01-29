#1차시도. 3분 소요.
# set도 iterable하다는 것을 알게 되었다.

class Solution(object):
    def intersection(self, nums1, nums2):
        nums1 = list(set(nums1))
        result = []
        for item in nums2:
            if (item in nums1) and (item not in result):
                result.append(item)
        
        return result