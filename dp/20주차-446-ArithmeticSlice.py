class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        total_count = 0  
        dp = [defaultdict(int) for _ in range(n)]

        # i가 끝 부분이고, j가 시작 부분
        # 만약 10을 돈다고 하면, 2,4,6,8이 나오는데,
        # 만약 6할때 diff가 4가 나와서 ok!라고 했는데,
        # 사실 6 10 이렇게 할때, 이전에 나왔던 -2 2 6 10 이렇게 있다고 하면. 
        # 이전에 나왔던 것들에다가 6 10 이 있는 경우를 더 해주면 된다.
        # 그거를 dp[i][diff] += dp[j][diff]에서 해주는 거고.
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                # 딱 그 두 원소만 있는 경우. 1을 더해준다.
                # 그리고 총 subsequence란. 결국 이전의 subsequence에다가 이 두 원소를 더한 것이다.
                dp[i][diff] += 1  
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    total_count += dp[j][diff]

        return total_count
    
# 2,4,6,8,10

# 10:03. 1차시도 실패.
# 2에서 시작. 2+n in dict? 2+2n in dict? 그러면 포함.
# 근데 이렇게 하면 3개만이잖아. 3개 이상인 경우는.
# n은 몇으로? idx 그 숫자부터 n-2까지의 숫자의 합.

# 5678910 이 된다.
# 글면. 678910부터 되는거를 셀 필요가 있을까?
# 8910의 경우는 어떤가? 5678910 에서 678이 포함된.
# 만들 수 있는 모든 subsequence에서, 5가 포함된 subsequence를 빼면 된다.
# 만들 수 있는 모든 subsequence는, 최소 3이상이어야 함.
# 그러면. 2**n - 10 - 5 - 1 => 32 - 16 = 16
# 즉 전체 2**len - nC2 - len - 1이렇게 해주면 됨.

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        cnt = 0
        for start in range(len(nums)):
            seen = {}
            start_val = nums[start]
            diff = []
            for end in range(start+1,len(nums)):
                seen[nums[end]] = True
                if end < len(nums) - 1:
                    diff.append(nums[end] - start_val)
            
            for df in diff:
                if start_val + df in seen and start_val + df*2 in seen:
                    cnt += 1
        
        return cnt