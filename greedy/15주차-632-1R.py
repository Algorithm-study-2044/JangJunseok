# 10:55시작.

# 배울 부분. 문제의 조건을 고정할 필요가 없다.
# 이산 value가 필요한 경우에는, array를 통한 통합과 sort를 통한 통합을 통해 이산화를 시킬 수 있다.


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        temp = []
        for i, arr in enumerate(nums):
            for val in arr:
                temp.append((val,i))
        
        temp.sort()
        k = len(nums)
        seen = defaultdict(int)
        ans = (temp[0][0],temp[-1][0])
        start = 0

        for val,idx in temp:
            seen[idx] += 1
            if len(seen) < k:
                continue
            else:
                # 이러면 이제 다 찼다는 것. start를 업데이트해보자.
                while len(seen) >= k:
                    if val - temp[start][0] < ans[1] - ans[0]:
                        # 이러면 더 작다는 거니까.
                        ans = (temp[start][0],val)
                    # 이제 start를 옮겨준다.
                    seen[temp[start][1]] -= 1
                    if seen[temp[start][1]] == 0:
                        del seen[temp[start][1]]
                    start += 1
        return ans
