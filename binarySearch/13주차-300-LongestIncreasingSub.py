# 1차시도. 다른 사람의 풀이 참고. 원래는 이해했으나, 이진탐색 자체가. 


# 2 5 3 4 이렇게 있으면, 전체는 3이 되어야 함. 어떻게? 
# 사실 n^2 시간복잡도면 간단한 문제이다. 그런데 그러면 시간초과가 날테니.

# [10,9,2,5,3,7,101,18]

# 2 5 3 7 101 에서, 2 5 가 들어간 담에 3을 넣어보자.
# 그러면 이 친구는 어디 들어가야 하는가?에서, 그걸 binary search 하자는 것이다.

# 2 5 3 7 101 에서, 5는 아 2의 오른쪽에 두세요. ㅇㅋ 
# 3은? 2의 오른쪽에 넣어야 해. 5보다는 왼쪽.
# 7은? 음..지금 2 3 이렇게 들어갔으니까, 3 오른쪽으로 넣읍시다! 이렇게.

class Solution(object):

    def binarySearch(self,target,arr):
        start = 0
        end = len(arr) -1

        while start != end:
            mid = (start+end) //2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                end = mid - 1
            else:
                start = mid +1

        return start

        # 이 이진탐색 자체가 잘못되었다. 여기다 적용하면 안된다.
        # [0]이 있을때, 1은 0 자리로 가야한다. 그런데 지금은 start를 반환해버리니까.
        
    def lengthOfLIS(self, nums):
        
        tails = [float("-inf")] * len(nums)
        # 근데 이 size는 왜 두는걸까?
        # 내 생각에는, 현재 넣은것의 length를 구하기 위해서.
        size = 0
        for x in nums:
            idx = self.binarySearch(x,tails[0:size+1])
            tails[idx] = x
            #만약에 x가 현재 list중 가장 컸다면, 그러면 늘어날것
            size = max(idx+1,size)
        
        # 만약에 더 작은것이 오면, tails의 맨 앞자리에 들어가고,
        # size는 다시 곱창날것.
        return size
        




# 2차시도. monotonic queue. 그러나 이런 문제가 있음.
# i 요소를 위해서 pop pop했을때
# 그게 i-1 요소에 영향을 주지 않을까?
# i-1이 i보다 크면, 문제가 없다. 왜? 어차피 작을테니까
# i-1이 i보다 작으면? 그러면 문제가 있지 않을까. 
# 가령 2, 5, 3, 4 가 있다고 치자. 그러면? 
# 2 입장에서는 3을 만들 수 있는데, 내 로직상으로는 2밖에 안되는 점.

class Solution(object):
    def lengthOfLIS(self, nums):
        dp = [0] * len(nums)
        queue = deque([])
        for i in range(len(nums)-1,-1,-1):
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
            dp[i] = len(queue)
        return max(dp)
    


# 3차시도. 




            
            