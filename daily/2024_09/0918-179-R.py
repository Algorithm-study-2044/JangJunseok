# 2차시도. 다른 사람의 풀이 참고.

# 3과 34 이렇게 있을때, 어느게 더 커요? 34가 더 커요. 3보다.
# 9 93 이렇게 있을때, 어느게 더 커요? 993이 더 커요. 939보다.  

# 그래서 하나로만 판단할 수 없고,
#

from functools import cmp_to_key

def largestNumber(nums):
    # Convert integers to strings
    nums = list(map(str, nums))
    
    # Define custom comparator
    def compare(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0
    
    # Sort using the custom comparator
    nums.sort(key=cmp_to_key(compare))
    
    # Handle the edge case where the largest number is "0"
    if nums[0] == '0':
        return '0'
    
    # Join the sorted list into a single string
    return ''.join(nums)

# Example usage
nums = [3, 30, 34, 5, 9]
print(largestNumber(nums))  # Output: "9534330"




# 11:10 시작. 1차시도 실패. 20분 소요. 왜? 접근이 잘못됨.
# 무조건 자리수가 적은게 유리할줄알았는데, 엣지케이스가 있었음.

# 계층을 만들 수 있지 않나
# 첫째자리로 순위 매기고, 그 다음 두번째로
# 그런데 문제는, 3과 34를 넣었을때, 끝에는 항상 -inf를 붙여준다.

# 9, 93
# 5
# 3, 34, 30

# 그 순위대로 꺼내면 된다.
# 음 근데..34가 먼저오고 3이 와야 한다.

# 34 3 이라는 건데,

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        heap = []
        for num in nums:
            arr = [-int(item) for item in str(num)]
            arr.append(float("-inf"))
            heapq.heappush(heap,arr)

        res = ""
        for i in range(len(heap)):
            curr = heapq.heappop(heap)
            curr.pop()
            res += "".join([str(-item) for item in curr])

        return res