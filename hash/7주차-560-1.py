# 1차시도. 실패. 왜? set을 쓴게 문제임.
# [0,0,0] k=0 이면, 6이 나와야 하는데, 3이 나온다.


class Solution(object):
    def subarraySum(self, nums, k):
        cnt = 0
        curr_sum = 0
        myset = set()

        for item in nums:
            curr_sum += item            
            if curr_sum == k:
                cnt += 1
            if curr_sum - k in myset:
                cnt += 1
            myset.add(curr_sum)
        return cnt
    

# 2차시도. time limit exceeded. 
# 왜? for문 안에서, 또 for문을 돌려서, O(n^2)가 되어버림.
# 그래서, O(n)으로 해결해야 한다.

class Solution(object):
    def subarraySum(self, nums, k):
        cnt = 0
        curr_sum = 0
        sums = []

        for item in nums:
            curr_sum += item            
            
            if curr_sum == k:
                cnt += 1

            for t in sums:
                if curr_sum - t == k:
                    cnt += 1
            
            sums.append(curr_sum)
        return cnt

# 이런식으로 다른사람들은 해결했다.
# 어차피 필요한거는 개수니까. 현재의 current_sum 이전에 나왔던 current_sum - k가 몇개인지만 알면 된다.
# 그래서 dict에 저장해놓고, current_sum - k가 있었던 횟수를 더해주면 된다.

# 나의 경우와는 어떻게 다르냐면. 나는 list를 다 돌면서 파악을 했었다. 
# 근데 그렇게 해버리면, 1,1,1,1 일때, 3번째에서도 루프를 다 도는데, 그 다음 4번째에서도, 루프를 다 돌아버리니까.
# 당연히 비효율적이다. 한번 계산한것을 또 계산해버리니까.


class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum = {0: 1}  
        current_sum = 0
        
        for num in nums:
            current_sum += num
            count += prefix_sum.get(current_sum - k, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        
        return count


# 고쳐보면.
# 어쨋거나 대상이 여러개 필요할때는, dict를 사용하자.   

class Solution(object):
    def subarraySum(self, nums, k):
        cnt = 0
        curr_sum = 0
        sums = {0:1}

        for item in nums:
            curr_sum += item            
        
            # 전체 합이 k가 되는 부분도 포함하나?
            # 어쨋거나 sums에는 지금 대상 이전의 합만 저장되는거 아닌가?
            # 그렇다. 그래서 array는 1부터 전체까지 저장할 수 있는것다.   
            cnt += sums.get(curr_sum - k, 0)
            sums[curr_sum] = sums.get(curr_sum, 0) + 1
        return cnt