# 11:05. 4651ms. 21.78% beats.

# 조건이 분기하는 경우가 있다. 예를 들어 a,b가 충돌할때, 
# a를 넣는다면 b는 못넣고, 
# 그런데 b를 넣는다면? a는 빠지겠지만, 또 b로 인해 빠지는것도 고려해야 하고
# 이런식으로 조건이 분기가 된다. 이런 경우에는 DFS를 사용하면 될 듯 하다.

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans = [0]

        def DFS(arr,seen):
            if len(arr) == 0:
                return

            # 현재 요소를 넣고 넘어가는 경우.
            if arr[0] - k not in seen and arr[0] + k not in seen:
                copied = seen.copy()
                copied.add(arr[0])
                ans[0] += 1
                DFS(arr[1:],copied)

            # 현재 요소를 넣지 않고 넘어가는 경우
            copied_2 = seen.copy()
            DFS(arr[1:],copied_2)

        DFS(nums,set())
    
        return ans[0]

