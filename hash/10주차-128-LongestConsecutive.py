# 08:45 1차시도. 13분. 실패. 시간초과. 시간복잡도는 O(n^2)이다.

from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nb = defaultdict(int)
        max_depth = [0]

        def DFS(number,depth,tp):    
            if number in nb:
                if tp == "increase":
                    DFS(number+1,depth+1, "increase")
                else:
                    DFS(number-1,depth-1, "decrease")
            else:
                depth -= 1
                max_depth[0] = max(depth, max_depth[0])

        for item in nums:
            nb[item] += 1
        
        for item in nums:
            DFS(item,1,"increase")
            DFS(item,1,"decrease")

        return max_depth[0]
    

# 2차시도. Editorial 참고
    
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

# 3차시도. 366ms. 54.93%. 

# 일단 item-1 item+1 이 아니라, 시작점만 두고 본다.
# set으로 보는 정도를 많이 줄였다. 시작점만 두고 보자는 거다.

from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        longest = 1
        hash_map = set(nums)

        def DFS(number,depth):
            nonlocal longest
            if number in hash_map:
                DFS(number+1,depth+1)
            else:
                depth -= 1
                longest = max(longest, depth)

        for item in hash_map:
            if item-1 not in hash_map:
                DFS(item+1,2)
        
        return longest
        


