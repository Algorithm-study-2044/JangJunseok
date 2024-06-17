# 1차시도. 실패. 어떻게 하면 이렇게 풀 수 있는지 다시풀어볼것.
# 다른 사람의 풀이 참고.

#Intuition
#The code works like providing change with limited coin denominations. Suppose you need to cover every amount up to 𝑛 cents. 
# If you can't make exact change for a particular amount miss, 
# it indicates you lack a coin of value less than or equal to miss. 
# To fill this gap, you add a coin of that exact missing amount. 
# This addition allows you to now cover new amounts up to 2 * miss. 
# Repeat this process until you can provide change for every amount up to 𝑛. 
# This method ensures you add the minimum number of new coins needed to cover any shortages.


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        result = 0
        i = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                # 내가 miss를 만들 수 없다. 그러면 1~miss-1까지는 만들 수 있다.
                # 그런데 nums[i]가 miss보다 작다? 그러면, 만들 수 없는 nums[i]의 범위는 그만큼 확장되는 것이다.
                # miss-1 + nums[i]까지 만들 수 있으니까, miss는 miss + nums[i]가 되어야 함.
                i += 1
            else:
                # 현재 만들 수 없는 miss를 추가한다.
                # 그 경우, 이제 miss는 확장된다. (miss ~ miss*2-1까지 만들 수 있게 된다.)
                # miss 이전까지는 다 만들 수 있다. 그러니까, miss를 더하면?
                # miss, miss+1, miss+2, ..., miss+miss-1까지 만들 수 있다.
                # 즉 만들 수 없는 최소한의 수는 miss*2로 확장이 된다는 것이다.
                miss += miss
                result += 1

        return result