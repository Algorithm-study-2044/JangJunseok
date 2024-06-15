# 11:17 시작. 1차시도. 시간초과. 실패.

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        seen = set()
        cnt = 0
        # nums.sort() 이거 넣어도 마찬가지.
        for num in nums:
            while num in seen:
                num += 1
                cnt += 1
            seen.add(num)
        return cnt
    
# 2차시도. 실패.

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        cnt = 0
        for num in nums:
            print(num,cnt)
            if num in seen:
                if seen[num] != num:
                    #이미 이사를 갔다?
                    # 문제는 이렇게 한칸 더 이사를 가면. 그거를 다시 seen에 넣어주어야 하는데.
                    # 그렇게 되는 경우. 2 -> 4 가고. 4 -> 5로 
                    # 즉 32244 이렇게 있을때. 업데이트가 이상하게 도어버림.
                    seen[num] += 1
                    cnt += seen[num] - num
                else:
                    # 처음 이사를 간다?
                    init = num
                    while num in seen:
                        num += 1
                        cnt += 1
                    seen[init] = num
            else:
                seen[num] = num
        return cnt
    

# 3차시도. 실패. 뭔가 sort를 활용해보려고 했는데. 잘 안되었음. 어떻게 하면 2222 이렇게 있을때. 2 -> 3 -> 4 -> 5 이렇게 이동하는걸로 바꿀수 있을까?
# 그 number가 되어야 하는 숫자를 찾는게 핵심인듯. 

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        combo = defaultdict(int)

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                nums[i] += combo[nums[i]] +1
                combo[nums[i]] += 1
                cnt += 1

        return cnt

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        numTracker = 0
        minIncreament = 0

        for num in nums:
            numTracker = max(numTracker, num)
            minIncreament += numTracker - num
            numTracker += 1
        return minIncreament