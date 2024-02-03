# 2주차. 15분 소요. pass. 28% beats.
# 2**n+k 번째는 1+k번째와 같다.
class Solution(object):

    def calc_max_two(self,n):
        start = 0
        while 2**(start+1) <= n:
            start += 1
        return 2**(start)

    def countBits(self, n):
        if n == 0:
            return [0]
        elif n == 1:
            return [0,1]
        else:
            ans = [0] * (n+1)
            ans[0] = 0
            ans[1] = 1

            for i in range(2,len(ans)):
                left = i - self.calc_max_two(i)
                ans[i] = 1 + ans[left]
            return ans