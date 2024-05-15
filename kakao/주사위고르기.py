#1차시도. 실패. 기댓값과 정렬을 활용한 풀이.

def solution(dice):
    
    def calc_expect(arr):
        sum = 0
        for i in arr:
            sum += i
        return sum / len(arr)
    
    def v_expect(arr,avg):
        sum = 0
        for i in arr:
            sum += (i-avg)**2
        return sum // len(arr)
        
    
    diff = []
    
    for idx, arr in enumerate(dice):
        avg = calc_expect(arr)
        var = v_expect(arr,avg)
        diff.append((idx+1,avg,var))
    
    diff.sort(key = lambda x: (-x[1],-x[2]))
        
    n = len(diff) // 2
        
    return [idx for idx, *arg in diff][:n]

#2차시도, 다른 사람의 풀이 참조.

from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    win_dict = {}
    L = len(dice)
    
    # 일단 a의 index 조합과 b의 index 조합을 고른다. 어떻게?
    for i in combinations(range(L),L//2):
        # 예를 들어 [1,3,4,5] 이렇게 나왔다고 하자.
        b_i = [idx for idx, _ in enumerate(range(L)) if idx not in i]
        # 얘네 둘을 만들어준다. A,B가 있는데, 
        # 얘네는 각 조합에 대해 나온 주사위 수의 합을 저장한다. 
        A = []
        B = []
        for order_of_product in product(range(6), repeat=L//2):
            # 이러면 이제 주사위의 조합 결정.
            # 그냥 A,B 매치 시킬 필요없이, 다 구해서 넣어주면 된다.
            # 그 이후의 이진탐색을 통해서 각각의 A 집합이 몇번 승리하는지를 구해주는게 핵심이다.
            
            A.append(sum(dice[i][j] for i,j in zip(i,order_of_product)))
            B.append(sum(dice[i][j] for i,j in zip(b_i,order_of_product)))
        
        B.sort()
        wins = sum(bisect_left(B,nums) for nums in A)
        win_dict[wins] = list(i)
        
    max_wins = max(win_dict.keys())
        
    return [i+1 for i in win_dict[max_wins]]