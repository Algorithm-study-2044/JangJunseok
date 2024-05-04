# 다른 사람의 풀이 연구.

# [1,3,2,4]

# r[2]값은 얼마겠냐? 그냥 3.
# l[2]는? 1.

# 결국 2를 최소로 가지는 친구는? 아니, 4개이다.
# 2, [3,2] [2,4] [3,2,4]

# 아 그래서, i-l[i]

class Solution(object):
    def sumSubarrayMins(self, arr):
        n = len(arr)
        l = [0] * n
        for i in range(n):
            l[i] = i-1
            while l[i] > -1 and arr[i] < arr[l[i]]:
                l[i] = l[l[i]]
        
        r = [0] * n
        for i in range(n-1,-1,-1):
            r[i] = i+1
            while r[i] < n and arr[i] < arr[r[i]]:
                r[i] = r[r[i]]
        
        res,m = 0,10**9+7
        for i in range(n):
            res += ((i-l[i])*(r[i]-i)*arr[i])
        
        return res % m



class Solution(object):
    def sumSubarrayMins(self, arr):
        l = [0] * len(arr)
        for i in range(len(arr)):
            l[i] = i - 1
            
            # l[i]는 내 바로 전의 인덱스, 다시 l[i]에 넣으면, 그 전의 인덱스. 이런식으로 계속 이전의 인덱스로 바꿔준다.
            # 그러면 최종적으로 담기는 l[i]는 인덱스가 담기는데, 그 인덱스는 arr[i]보다 큰 값이 담겨있는 인덱스가 담기게 된다.
            while l[i] > -1 and arr[i] < arr[l[i]]: 
                l[i] = l[l[i]]

        r = [0] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            r[i] = i + 1

            # 이번에는 오른쪽을 보자.
            # 첫번째는 패스하고, 그 다음걸 봤는데, 
            # 그래서 최종적으로 r[i]에 담기는 값은, arr[i]보다 큰 값이 담겨있는 인덱스가 담기게 된다. 
            # 근데 또 작았다가 커져버리면, 그 뒤에 값이 크다고 하더라도 안담긴다. 즉 이것도 monotonic stack이라고 할 수 있을것임.
            while r[i] < len(arr) and arr[i] <= arr[r[i]]: 
                r[i] = r[r[i]]

        res, m = 0, 10**9 + 7

        # 예를 들어 i=2였다고 치자. 그러면. 

        # 이건 뭘 계산하는가? arr[i]를 최소로 가지는 arr가 몇개 있어용? 이런 의미인듯 한데.
        for i in range(len(arr)):
            res = (res + (i - l[i]) * (r[i] - i) * arr[i]) % m

        return res