# 고민하다 못풀어서 다른 사람 풀이 봄.

from itertools import permutations
def check():
    pass

def solution(n, weak, dist):

    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    
    answer = len(dist) + 1  

    for start in range(length):
        for workers in list(permutations(dist, len(dist))):
            count = 1   
            position = weak[start] + workers[count - 1]
            
            for index in range(start, start+length):
                
                if position < weak[index]:
                    count += 1  
                    if count > len(dist):   
                        break
                    position = weak[index] + workers[count - 1]
            answer = min(answer, count)
        if answer > len(dist):
            return -1
    return answer

print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
