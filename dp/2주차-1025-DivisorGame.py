#2주차 pass. 중간에 문법 에러. n-j가 아니라 i-j겠지, 디버깅 잘하자..
#150ms. 5% beats. 느리다. 브루트 포스 썼는데. 다른 방법을 찾아보자.
#다른 사람 풀이를 보니, 홀수면 무조건 진다. 짝수면 무조건 이긴다. 이런 방법도 있다.
#내가 문제 이해를 잘못한듯. 5 -> 1 이 아니라, 5 -> 4 인데. 

class Solution(object):
    def divisorGame(self, n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            arr = [False] * (n+1)
            arr[1] = False
            arr[2] = True
            for i in range(3,n+1):
                flag = False
                for j in range(1,i):
                    if arr[i-j] == False and i % j == 0:
                        flag = True
                arr[i] = flag
            return arr[n]