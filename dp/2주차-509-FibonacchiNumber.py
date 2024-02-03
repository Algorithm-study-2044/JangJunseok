#2주차. 6분 소요. pass. 15ms. 71% beats.
class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            arr = [0] * (n+1)
            arr[1] = 1
            for i in range(2,n+1):
                arr[i] = arr[i-1] + arr[i-2]
            return arr[n]
        
# 다른 사람의 답. 미리 만들지 말고, append로 만들어나가는 방법.
class Solution:
    def fib(self, n: int) -> int:
        memo = [0,1]
        if n <= 1 :
            return n
        for i in range( 2, n+1 ):
            memo.append( memo[i-1] + memo[i-2] )
        return memo[-1]        