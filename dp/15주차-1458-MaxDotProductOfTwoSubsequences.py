# 다른 사람의 풀이 참고.

class Solution:
    def maxDotProduct(self, nums1, nums2):
        dp = [[-1] * len(nums2) for _ in range(len(nums1))]
        nums1Size = len(nums1)
        nums2Size = len(nums2)

        def calculateDotProduct(idx1, idx2):
            if idx1 == nums1Size or idx2 == nums2Size:
                return 0

            if dp[idx1][idx2] != -1:
                return dp[idx1][idx2]

            # 두 내적을 구하는 방법은, 둘다 포함. 왼쪽포함. 오른쪽 포함.
            option1 = nums1[idx1] * nums2[idx2] + calculateDotProduct(idx1 + 1, idx2 + 1)
            option2 = calculateDotProduct(idx1, idx2 + 1)
            option3 = calculateDotProduct(idx1 + 1, idx2)

            dp[idx1][idx2] = max(option1, option2, option3)
            return dp[idx1][idx2]

        firstMax = float('-inf')
        secondMax = float('-inf')
        firstMin = float('inf')
        secondMin = float('inf')

        for num in nums1:
            firstMax = max(firstMax, num)
            firstMin = min(firstMin, num)

        for num in nums2:
            secondMax = max(secondMax, num)
            secondMin = min(secondMin, num)

        # 하나는 다 음수이고 하나는 다 양수이다? 그러면, 최대한 크게 나올 수 있는 값을 return한다.
        if (firstMax < 0 and secondMin > 0) or (firstMin > 0 and secondMax < 0):
            return max(firstMax * secondMin, firstMin * secondMax)

        return calculateDotProduct(0, 0)



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
