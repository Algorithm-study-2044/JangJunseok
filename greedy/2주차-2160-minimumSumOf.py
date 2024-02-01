#2주차. 25분 소요. pass. 28%. beats 다시 풀어볼것.

class Solution(object):
    def minimumSum(self, num):
        num = [int(d) for d in str(num)]
        arr = sorted([item for item in num if item != 0])
        if len(arr) == 1:
            return arr[0]
        elif len(arr) == 2:
            return arr[0] + arr[1]
        elif len(arr) == 3:
            return arr[0] * 10 + arr[1] + arr[2]
        else:
            return arr[0] * 10 + arr[-1] + arr[1] * 10 + arr[-2]