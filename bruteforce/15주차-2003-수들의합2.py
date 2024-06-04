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