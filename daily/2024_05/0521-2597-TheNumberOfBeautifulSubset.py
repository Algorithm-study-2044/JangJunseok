# 11:38 시작. 다시 풀어볼 것.

# 2를 넣고 시작
# 그 다음 4를 넣고 시작.
# 1차시도. 실패. 
# [1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000]
# 에서 막혔다. 다른거 다 되는데.

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        cnt = [0]
    
        def DFS(start,seen):
            if start == len(nums):
                if len(seen) != 1:
                    cnt[0] += 1
                return
            
            for end in range(start,len(nums)):
                if nums[end] - k not in seen and nums[end] + k not in seen:
                    new_seen = seen.copy()
                    new_seen.add(nums[end])
                    DFS(end+1,new_seen)

            cnt[0] += 1
        
        DFS(0,set())

        return cnt[0]
    
# 해당 시점에서, 그걸 포함한 배열과, 포함하지 않은 배열을, 
    


# 해당 시점에서, 그걸 넣고 진행하는 것 하고
# 그걸 넣지 않고 진행하는 것.

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # nums = [2,4,6]
        # k = 2
        # [], [2], [4], [6], [2, 4], [2, 6], [4, 6], [2, 4, 6]
        # [2], [4], [6], [2, 6] -> 4 ans
        # SOLUTION
        # num - k or n + k

        count = 0
        lenNums = len(nums)

        def explore(index):
            nonlocal count
            if lenNums == index:
                count += 1
                return

            num = nums[index]

            if num - k not in visited and num + k not in visited:
                visited[num] += 1
                explore(index + 1)
                # 그 다음에, 이걸 빼줘야지만, index를 뺀 값을 explore할 수 있음.
                visited[num] -= 1
                if visited[num] == 0:
                    del visited[num]

            explore(index + 1)

        visited = defaultdict(int)
        explore(0)
        return count - 1


        