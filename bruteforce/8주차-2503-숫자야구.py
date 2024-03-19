# 1차시도. 실패. 다른사람의 풀이 참고.

import sys
from itertools import permutations

N = int(sys.stdin.readline().rstrip())

numbers = list(permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 3))

# n번 반복하면서, 정해진 숫자의 풀에서 strike, ball을 비교해서 맞지 않는 후보들을 제거한다.

for _ in range(N):
    question_number, strike, ball = map(int, sys.stdin.readline().split())
    question_number = list(str(question_number))
    removed = 0
	
    for i in range(len(numbers)):
        strike_cnt = 0
        ball_cnt = 0
        
        #이거는 이 안쪽 for문 안에서 i가 다른것을 가리킬 가능성이 높기 때문에.
        i -= removed
        
        for j in range(3):
            if question_number[j] == numbers[i][j]:
                strike_cnt += 1
            elif question_number[j] in numbers[i]:
                ball_cnt += 1
        
        if strike_cnt != strike or ball_cnt != ball:
            numbers.remove(numbers[i])
            removed += 1

print(len(numbers))