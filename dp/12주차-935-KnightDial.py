# 2차시도. 1차시도의 오류 수정 후 성공함.

class Solution(object):
    def knightDialer(self, n):
        if n == 1:
            return 10

        dp = [[0] * n for _ in range(10)]

        dial = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        def DFS(num, length):
            if length == 1:
                return 1

            # 저장된게 있으면 그걸 준다.
            if dp[num][length - 1] != 0:
                return dp[num][length - 1]

            # 저장된게 없으면 해당 스텝으로 갈 수 있는것들을 계산해서, 더하고 저장한다.
            # 그리고 그걸 반환한다.
            res = 0
            for i in dial[num]:
                res += DFS(i, length - 1)
                res %= (10**9 + 7)
                
            dp[num][length - 1] = res
            return res

        answer = 0

        for i in range(10):
            if i == 5:
                continue
            answer += DFS(i, n)

        return answer % (10**9 + 7)


# 1차시도에서 살짝 수정

dial = {
    1: [6,8],
    2: [7,9],
    3: [4,9],
    4: [3,9,0],
    6: [1,7,0],
    7: [2,9],
    8: [1,3],
    9: [2,4],
    0: [4,6],
}


class Solution(object):
    def knightDialer(self, n):
        if n == 1:
            return 10

        dp = [[0]*n for _ in range(10)]

        def DFS(num, length):
            if length == 1:
                return 1
                
            # 해당 계산된게 있을 경우에는. 그걸 반환한다.
            elif dp[num-1][length-1]:
                return dp[num-1][length-1]

            else:
                res = 0
                for i in dial[num]:
                    res += DFS(i,length-1)
                    res %= (10**9+7)
                dp[num-1][length-1] = res
                return res
    
        answer = 0

        for i in range(0,10):
            if i == 5:
                continue
            
            answer += DFS(i,n)
        
        return answer % (10**9+7)    
    


# 1차시도. 실패. 원리는 맞는것같은데 답이 안나오네..



dial = {
    1: [6,8],
    2: [7,9],
    3: [4,9],
    4: [3,9,0],
    6: [1,7,0],
    7: [2,9],
    8: [1,3],
    9: [2,4],
    0: [4,6],
}



# n=3일때는. 

class Solution(object):
    def knightDialer(self, n):
        if n == 1:
            return 10

        dp = [[0]*n for _ in range(10)]

        def DFS(num, length):
            if length == 2:
                return len(dial[num])
                
            # 해당 계산된게 있을 경우에는. 그걸 반환한다.
            elif dp[num-1][length-1]:
                return dp[num-1][length-1]

            else:
                res = 0
                for i in dial[num]:
                    k = DFS(i,length-1)
                    dp[i-1][length-2] = k
                    res += (k%10**9+7)
                return res
    
        answer = 0

        for i in range(0,10):
            if i == 5:
                continue
            
            answer += DFS(i,n)
        
        return answer % (10**9+7)    
    


# 2차시도. 다른 사람의 풀이 체크

class Solution(object):
    mod = 10**9 + 7
    MOVES = [
        [4, 6],
        [6, 8],
        [7, 9],
        [4, 8],
        [0, 3, 9],
        [],
        [0, 1, 7],
        [2, 6],
        [1, 3],
        [2, 4]
    ]

    def __init__(self):
        self.cache = [[0] * 10 for _ in range(5001)]

    def knightDialer(self, n):
        next_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        return self.knightDialerRecursive(n, next_numbers)

    def knightDialerRecursive(self, remaining, next_numbers):
        if remaining == 1:
            return len(next_numbers)

        count = 0
        for next_number in next_numbers:
            cur = self.cache[remaining][next_number]
            if cur == 0:
                cur = self.knightDialerRecursive(remaining - 1, self.MOVES[next_number])
                self.cache[remaining][next_number] = cur
            count += cur
            count %= self.mod

        return count
    

