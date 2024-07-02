# 4:15 시작. 1차시도. 실패. 

# 그러니까 1 + 2 + 3일때. 브루트포스면, 1+2+3 2+3 이렇게 가는건데
# 굳이 2+3을 두번 더해줄 필요가 있나? 1+2+3할때, 이전 조합가지고 지금 나머지를 뗄 수 있다면
# 그러면 한번의 루프로 계산해줄 수 있다는 것이다.

# 아 이거. 560번과 비슷하다. 
# 즉 (prefix_sum - x) % k == 0 이 되는 x가 있나요? 그러면 그 x를 빼주면 k의 배수가 되는거니까.

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_map = {0: 1}  
    
    # 1 2 3 인 경우에.
    # 1개 나와야 하는데.

    # 결국 붙어있는 놈이라는거는. 
    
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            if mod < 0:  
                mod += k

            if mod in prefix_map:
                count += prefix_map[mod]
                prefix_map[mod] += 1

            else:
                prefix_map[mod] = 1
        
        return count




class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        modulo_dict = defaultdict(int)
        idx_dict = {}

        for i in range(len(nums)):
            idx = nums[i] % k
            left = k - (nums[i] % k) if nums[i] % k != 0 else 0
            insert = modulo_dict[left]
            modulo_dict[idx] += 1
            idx_dict[nums[i]] = insert
        
        res = 0
        for i in range(len(nums)):
            left = k - (nums[i] % k) if nums[i] % k != 0 else 0
            res += (modulo_dict[left] - idx_dict[nums[i]])
            # res에 더 더해줘야 한다는 것이다. 
        return res
    

    class Solution:
        def subarraysDivByK(self, nums: List[int], k: int) -> int:
            count = 0
            n = len(nums)
            
            for i in range(n):
                curr_sum = 0
                for j in range(i, n):
                    curr_sum += nums[j]
                    if curr_sum % k == 0:
                        count += 1
            
            return count