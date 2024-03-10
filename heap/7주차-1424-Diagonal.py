#1차시도. 실패. 잘못된 답.

class Solution(object):
    def findDiagonalOrder(self, nums):
        res = []
        for i in range(0,len(nums)):
            for j in range(i+1):
                if len(nums[i-j]) -1 >= j:
                    res.append(nums[i-j][j])        
        
        for i in range(len(nums)-1,0,-1):
            for j in range(i+2):
                if len(nums[i]) -2 >= j:
                    res.append(nums[i][1+j])

        return res
    
#2차시도. 다른 사람의 풀이 연구.
#결국 같은 곳에 들어가는 애들은 뭐다? x,y좌표의 합이 같은 애들이다.
#그러면 그 x,y좌표의 합에 해당하는 []는 몇개 있어야 하나? x+y = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 이렇게 16개다.
#
    
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        n = max(len(x) for x in nums)
        bucket = [[] for _ in range(m+n-1)]
        #뒤에서부터 넣는 이유는, 이게 왼쪽 아래에서 오른쪽 위로 대각선으로 가로지르는거니까.
        for i in range(m-1, -1, -1):
            for j, x in enumerate(nums[i]):
                bucket[i+j].append(x)
        ans = []
        for x in bucket: ans += x
        return ans