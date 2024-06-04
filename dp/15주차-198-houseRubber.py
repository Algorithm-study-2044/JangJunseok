# 11:20. 36ms. 54% beats. 

# 그냥 한칸 띄우고 다시 훔치고, 다시 훔치고 하면 되잖아?
# 그게 그렇게 간단하지는 않은게, 예를 들어 홀수번만 훔치고 싶은데,
# 그러다가 짝수번 훔치고 싶으면. 그럴 수도 있는것임.

# 1 2 3 4 5 6 7 8
# 1 3 5 7 이렇게 가지 않고 1 4 6 8 이런식으로.
# 그보다 더 멀리갈 수도 있나? 없다. 1 5 이러면 3을 추가하는것보다 나을게 없다.

# 그러니까 4번 입장에서는, 2에서 오는게 더 클지 아니면,
# 1번에서 바로 오는게 더 클지를 계산.

# 그렇게 해서 마지막 두개를 비교하면 되지 않을까.

class Solution:
    def rob(self, nums: List[int]) -> int:
        k = len(nums)
        dp = [0] * k

        if k == 1:
            return nums[0]

        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(k):
            if i >= 2:
                dp[i] = dp[i-2] + nums[i]
            
            if i >= 3:
                dp[i] = max(dp[i-3] + nums[i], dp[i])

        return max(dp[-1],dp[-2])