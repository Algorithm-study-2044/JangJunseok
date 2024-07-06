# 2:15 시작. 22분 소요. 269ms. 78.91% beats.

# 난이도 59% 짜리 문제.

# 정렬한다음에, 왼쪽 오른쪽 비교한다. 더 크기가 작은쪽을 바꿔준다. -> 이건 그리디임.
# 그런데 총 3번의 경우. 즉 하나의 시행이 다른 시행에 영향을 미칠 수 있기 때문에,
# 이걸 변경해줬음. 왼쪽0 오른쪽3 -> 왼쪽1 오른쪽2 -> 왼쪽2 오른쪽1 -> 왼쪽3 오른쪽0 이런식으로 다 계산한다음에 비교.

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 4:
            return 0
        
        maxVal = 0

        for i in range(4):
            current = 0
            for left in range(i):
                current += nums[left+1] - nums[left]
            for right in range(3-i):
                current += nums[-right-1] - nums[-right-2]
            maxVal = max(maxVal, current)
        
        return nums[-1] - nums[0] - maxVal