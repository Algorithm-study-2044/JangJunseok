# 6:22 시작. 10분 소요. 582ms. 38.65% beats.

# 11 두번 돈다음에, 남은건 0.
# 이제 이거를 prefix_sum으로 찿아주면 된다.
# 5가 남는데, 이거는 두번째에서 over이니까 그걸 찾아주는 식으로.

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sums = sum(chalk)
        left = k % sums
        prefix_sums = 0
        for idx,val in enumerate(chalk):
            prefix_sums += val
            if prefix_sums > left:
                return idx