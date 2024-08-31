import math

# 에라토스테네스의 체 알고리즘을 통해서 소수를 구해보자.
n = int(input())
array = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제와)

# 원래 1~n에서부터 구고 싶으면. n이면 되는데,
# n+1 해줬다. 왜? idx 맞추기 편하게 하기 위해서.

# 0,1은 소수 아님.
array[0] = False
array[1] = False

for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1


# n이하의 소수를 모두 구해주었음
sosu = [item[0] for item in enumerate(array) if item[1] == True]

# 그 다음 투포인터로 소수의 연속합 가능한걸 다 찾아보자.
l = 0
r = 0
cnt = 0
curr = 0
t = len(sosu)

while l <= t-1:
    if curr >= n:
        if curr == n:
            cnt += 1
        curr -= sosu[l]
        l += 1
    elif curr < n:
        if r <= t-1:
            curr += sosu[r]
            r += 1
        # 더 이상 늘릴 수 없다. l은 늘려봤자이고. 여기서 멈추셈.
        else:
            break

print(cnt)