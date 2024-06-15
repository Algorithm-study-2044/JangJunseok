# 다른 사람의 풀이 참고.. 그러나 잘 모르겠다. 다시 볼 것.

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        if m < n:
            return self.maxDotProduct(nums2, nums1)
        
        dp = [float("-inf")] * (n + 1)
        
        for i in range(m):
            prev = 0
            for j in range(n):
                tmp = dp[j + 1]
                dp[j + 1] = max(prev + nums1[i] * nums2[j], nums1[i] * nums2[j], dp[j], dp[j + 1])
                prev = tmp
        r
        return dp[-1]
