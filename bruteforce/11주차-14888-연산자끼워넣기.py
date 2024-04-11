# 다른 사람의 풀이 참고.

import sys

input = int(input())
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, minus, multiple, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(maximum, total)
        minimum = min(minimum, total)
    
    if plus:
        dfs(depth+1, total+num[depth], plus-1, minus, multiple, divide)
    if minus:
        dfs(depth+1, total-num[depth], plus, minus-1, multiple, divide)
    if multiple:
        dfs(depth+1, total*num[depth], plus, minus, multiple-1, divide)
    if divide:
        dfs(depth+1, total/num[depth],plus,minus, multiple, divide-1)
    
dfs(1,num[0],op[0],op[1],op[2],op[3])

print(maximum)
print(minimum)

    

# 그러한 담론은 어느 개인이 만들어내어서, 유포된것이 아니다.
# 애초에 맥락없이 등장한 담론이었다면, 그게 사람들에게 받아들여지지도 않았을거다.
# 사람들이 막연하게 생각하고 있던 것에, 이름을 붙여준거다. 그런식으로밖에 생각하지 못하도록.

