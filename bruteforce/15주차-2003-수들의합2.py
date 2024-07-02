# 10 5
# 1 2 3 4 2 5 3 1 1 2

# 그런데 left <= right 이렇게 하면, 둘이 같고 딱 동일할때가 안되지 않나?
# 그러므로 match할때는, 그냥 right를 +1해주면 ok인거다. 그러면 커질텐데? 아니. 그래도 그 다음 로직에서 판별이 될테니까.

# 내가 고민하는 부분은, 요소가 1이고, 그 요소가 target보다 클때, 이걸 어떻게 처리하냐는 것이다.
# right는 포함하지 않는 걸로 고려를 하면 된다. 왜? 그러면 최악의 경우 len=0이니까 다시 right가 늘어나서 둘이 교차할 가능성은 없다.

_,target = map(int,input().split())
arr = list(map(int,input().split()))

left = 0
right = 1
N = len(arr)
res = 0
curr = arr[0]

while left <= right and right <= N:
    # left = N일때도 들어갈 수는 있지만 curr == target이거나, curr > target일 수가 없다.
    if curr == target:
        curr -= arr[left]
        left += 1
        res += 1

    elif curr > target:
        curr -= arr[left]
        left += 1
    
    elif curr < target:
        # 왜? right == N일때도 들어갈건데, 이때는 확장되면 안되고 축소만 가능하다.
        if right <= N-1:
            curr += arr[right]
        right += 1

print(res)




# 1차시도. 

_,target = map(int,input().split())
arr = list(map(int,input().split()))

left = 0
right = 1
curr = arr[0]
res = 0

# 밑에 있는거는. 일단 체크하고 -> 그 다음에 array 범위 내에 있는지를 판단한다.

while left <= right and right <= len(arr):

    if curr == target:
        res += 1
        curr -= arr[left]
        left += 1

    elif curr > target:
        curr -= arr[left]
        left += 1
    
    elif curr < target and right < len(arr):
        curr += arr[right]
        right += 1
        
    # 여기서 else break 조건은, curr <target 이기는 하지만 right가 넘어가서 break 해주어야 하는 것.
    else:
        break

print(res)


# 이렇게 수정되어야 함.

_, target = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
curr = 0
res = 0

# 일단 len(arr) 안에만 있으면 패스하도록 함.

while right <= len(arr):
    if curr == target:
        res += 1
        curr -= arr[left]
        left += 1
    elif curr > target:
        curr -= arr[left]
        left += 1
    # 그리고 이제 여기서 검사하도록 함.
    elif curr < target and right < len(arr):
        curr += arr[right]
        right += 1
    else:
        break

print(res)


# 비슷한 풀이.

n, m = map(int, input().split())
a = list(map(int, input().split()))

sum = a[0]
left = 0
right = 1
cnt = 0

while True:

    if sum < m:
        if right < n:
            sum += a[right]
            right += 1
        else:
            break

    elif sum == m:
        cnt += 1
        sum -= a[left]
        left += 1

    else:
        sum -= a[left]
        left += 1

print(cnt)


# 결국 다른 사람의 풀이 참조. 푸는 방법은 맞았다. 
# 근데 이거는 좀 비효율적일것같다.

N, M = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 1
cnt = 0
while right<=N and left<=right:

    sum_nums = nums[left:right]
    total = sum(sum_nums)

    if total == M:
        cnt += 1
        right += 1

    elif total < M:
        right += 1

    else:
        left += 1

print(cnt)