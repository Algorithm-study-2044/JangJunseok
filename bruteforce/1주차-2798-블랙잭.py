#1차시도. 브루트포스. pass. 72ms.

import sys
n,m = map(int,input().split())

arr = list(map(int,sys.stdin.readline().split()))

maxNum = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sumOf = arr[i] + arr[j] + arr[k]
            if maxNum < sumOf and sumOf <= m:
                maxNum = sumOf

print(maxNum)



#2차시도. sliding window. pass. 40ms

import sys
n,m = map(int,input().split())

arr = sorted(list(map(int,sys.stdin.readline().split())))

maxNum = 0

def get_two_sum(arr,selected):

    global maxNum

    target = m - selected

    if len(arr) < 2 or arr[0] + arr[1] > target or arr[-1] + arr[-2] + selected < maxNum:
        return

    l,r = 0,len(arr)-1

    while l < r:
        two_sum = arr[l] + arr[r]
        if two_sum < target:
            if two_sum + selected > maxNum:
                maxNum = two_sum + selected
            l += 1
            while l > 0 and arr[l] == arr[l-1]:
                l += 1
        elif two_sum == target:
            maxNum = selected + two_sum
            return
        elif two_sum > target:
            r -= 1
            while r < len(arr) and arr[r] == arr[r-1]:
                r -= 1    

for i in range(len(arr)):
    get_two_sum(arr[i+1:],arr[i])

print(maxNum)
    
