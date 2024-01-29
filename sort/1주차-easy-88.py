# 뭔가 이상해서 정답 봄.
# 이렇게 하면, num1의 값이 바뀌지 않는다.
# 아마 함수 안에서 새로운 변수를 만들어서 그걸 바꾸는 것 같다.

# 그런데 nums1[0] = df 이렇게 하면, 그 값이 바뀌어진다.
# 혹은 nums1.sort() 이렇게 하면, 그 값이 바뀌어진다.
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        arr = nums1[:m] + nums2[:n]
        arr.sort()
        nums1 = arr

#그러므로 이렇게.
        
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:] = nums1[:m] + nums2[:n]
        nums1.sort()