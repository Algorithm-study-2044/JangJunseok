# 3:26 -> 3:40. 버블 정렬. 35ms. 73% beats.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for t in range(len(nums)-1):
            for i in range(1,len(nums)-t):
                if nums[i] < nums[i-1]:
                    nums[i],nums[i-1] = nums[i-1],nums[i]
        
        return nums

# 다른사람의 풀이. 1. counting sorts.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq=[0]*3
        for x in nums: freq[x]+=1
        count=0
        for x in range(3):
            nums[count:count+freq[x]] = [x]*freq[x]
            count+= freq[x]


# 또 다른 풀이.

# class Solution {
# public:
#     void sortColors(vector<int>& nums) {
#         //Dutch national flag problem (red, white, blue)
#         const char red=0, white=1, blue=2;
#         int l=0, m=0, r=nums.size()-1;// pointers to partition
#         while(m<=r){
#             switch(nums[m]){
#                 case red:
#                     swap(nums[l], nums[m]);
#                     l++, m++;
#                     break;
#                 case white:
#                     m++;
#                     break;
#                 case blue:
#                     swap(nums[m], nums[r]);
#                     r--;
#             }
#         }
#     }
# };

# );

        