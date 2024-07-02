# 3분소요. 42ms 88.36% beats.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = defaultdict(int)
        for i in nums1:
            seen[i] += 1

        res = []
        for i in nums2:
            if i in seen and seen[i]:
                res.append(i)
                seen[i] -= 1
                
        return res
        
        