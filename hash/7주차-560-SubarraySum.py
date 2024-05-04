#1차시도. 시간초과. 
class Solution(object):
    def subarraySum(self, nums, k):

        cnt = 0

        for idx in range(1,len(nums)):
            for end in range(idx,len(nums)):
                if sum(nums[idx:end+1]) == k:
                    cnt += 1
                    continue    
        
        return cnt


#2차시도. 다른사람의 풀이 연구.

# curremt_sum은 결국 prefix_sum의 key값 + 얼마 인데.
# 즉 b = a + k 에서, b - k = a이고, 이때 a값이 있었다고 한다면,
# b - a = k가 되기 때문에, b값을 만나면, b - k값이 있었는지 확인하면 된다.
# 그럼 이때, b - k값이 있었다면, 왼쪽부분을 떼서 오른쪽 부분으로 k를 만들 수 있다는 뜻이다.
# 이렇게 함으로써 한번만 루프를 돌면서도 모든 경우의 수를 확인할 수 있다.
    
class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum = {0: 1}  
        current_sum = 0
        
        for num in nums:
            current_sum += num
            count += prefix_sum.get(current_sum - k, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        
        return count


        