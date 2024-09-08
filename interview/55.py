# 11:06. 20분 소요. 38.8%짜리 성공!!. 364ms. 45.07% beats.

# 해당 지점에서, 마지막 인덱스가 범위 내에 있으면 가능하긴 한데
# 만약 그렇지 않다면? 범위 내 지점들 중에서 가장 큰놈을 찾으면 되는거 아닐까?
# 범위내 2 0 0 1 이렇게 되어 있다면, 안됨. 1을 택하는게 맞음.

# 결국 DFS로 풀어야 하는걸까? 왜냐하면 범위를 벗어나면서, 각각 도달할 수 있는 범위도 여러개 있잖아.
# 아니 그 중에 우열을 가릴 수 있다. 
# 내 범위를 더 확장시켜줄 수 있는 사람을 골라야 한다. 만약 그게 여러개 있다면
# 그 중에서 더 확장시켜줄 수 있는 친구로. 그러니까 단순히 숫자가 큰거랑은 다르다.

# 그 범위를 확장시켜줄 수 있는 사람이 없다면? False.
# 0 -> 3까지. 그러면 3까지 가면서, -1 + 범위 한게 3보다 큰게 있는가?
# 있으면 그걸 지점으로, 

# 일단 기준에서 범위를 구한다. 그게 last index? 그럼 True
# last index는 아니고, 그러면 기준+1 ~ 범위를 쭉 돌면서, 
# 해당 idx + range > 마지막 범위

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = 0
        end = nums[0]

        while end < len(nums) - 1:
            max_end = end
            for i in range(start+1,end+1):
                if i + nums[i] > max_end:
                    max_end = i + nums[i]

            if end == max_end:
                return False

            start = end
            end = max_end

        return True