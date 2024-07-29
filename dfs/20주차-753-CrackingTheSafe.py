# k=4 n=2이면?
# 00 ~ 03
# 10 ~ 13
# 30 ~ 33 이렇게 됨.
# 30 31 32 33

# 그 다음 0으로 시작하는거 찾는다. 있으면 붙여준다.. 없으면? 붙이지 말고 그냥. 아무거나 집어서,
# 근데 이 있으면 붙여주는것도, 지능적으로 해야하지 않나?

# k는 나올수있는 숫자범위. n은 패스워드 길이.

# n은 2, k는 1이라고 해보자.


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return ''.join([str(i) for i in range(k)])
        if k == 1:
            return '0' * n
        suffix_map = {}
        all_combinations = ['0']*(n-1)
        for _ in range(k**n):
            suffix = ''.join(all_combinations[1-n:])
            suffix_map[suffix] = suffix_map.get(suffix, k) - 1
            all_combinations.append(str(suffix_map[suffix]))
        return ''.join(all_combinations)