#1차시도. 그냥 combinations 사용함.

cases = []

while True:
    a = list(map(int,input().split()))
    if a[0] == 0:
        break
    cases.append(a)
    
    
from itertools import combinations

def handle_case(case):
    arr = case[1:]
    nCr = combinations(arr,6)

    for item in nCr:
        for c in item:
            print(c,end=' ')
        print("\n")

for case in cases:
    handle_case(case)
    print("\n")


# 재귀를 활용한 풀이.
# 0 1 2 3 4 5 6

# 마지막 5일때, 넘어가서, 6찍고, print하고, 다시 pop하고

# 즉 idx0넣어서 시작하고, 
# 

def dfs(depth, idx):
    if depth == 6:
        print(*out)
        return

    for i in range(idx, k):
        out.append(S[i])
        dfs(depth + 1, i + 1)
        out.pop()


while True:
    array = list(map(int, input().split()))
    k = array[0]
    S = array[1:]
    out = []
    dfs(0, 0)
    if k == 0:
        exit()
    print()