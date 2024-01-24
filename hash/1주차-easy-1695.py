# 우선 첫번째로, python의 global 개념과 for 블록변수 개념을 제대로 알지 못해서
# 잘못 풀었었고, 그게 시간을 좀 잡아먹었다.
# 두번째는 이렇게 브루트 포스로 푸니까, 시간초과가 나왔다.
class Solution(object):
    def maximumUniqueSubarray(self, nums):
        global maxNum
        maxNum = 0
        for index, value in enumerate(nums):
            unique = {}
            result = 0
            for j in range(index,len(nums)):    
                if nums[j] not in unique:
                    unique[nums[j]] = True
                    result += nums[j]
                    # 마지막이면 이제 maxNum과 비교하고 끝내야 함.
                    if j == (len(nums) - 1):
                        maxNum = max(maxNum, result)
                        break
                else:
                    #중복 있으니까 멈춰야 함.
                    maxNum = max(maxNum, result)
                    break
                
        return maxNum
    
# 다른 사람의 답.
    
# 여기서 l이라는건, 겹치는 두 숫자가 있을때,
# 그 중에서 한칸 더 앞에 있는 숫자의 인덱스를 의미한다.
class Solution:
    def maximumUniqueSubarray(self, nums) -> int:
        seen = set()
        curr_sum, max_sum, l = 0, 0, 0
        for num in nums:
            #그러니까 새로운 원소를 더했을때, 가장 큰 합이 될 수 있는걸 curr_sum에 저장하고,
            # max_sum에는 그 중에서 가장 큰걸 저장한다.
            # l은 그냥, 겹치는게 있으면, 그 이전거를 다 잘라내야 하니까, 
            # 잘라낸 이후의 시작 인덱스

            # l은 그 이전꺼를 볼 필요가 없다.
            # max_sum이 그 이전꺼라고 하더라도,
            # l은 그냥 현재의 curr_sum을 구하기 위한 인덱스일 뿐이다.

            # 겹치는게 있어버리면, 그 이전거를 다 잘라내야 한다.
            while num in seen:
                curr_sum -= nums[l]
                seen.remove(nums[l])
                l += 1
            curr_sum += num
            seen.add(num)
            max_sum = max(max_sum, curr_sum)

        return max_sum