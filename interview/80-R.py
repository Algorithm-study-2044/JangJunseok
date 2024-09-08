# 2차시도. 다른 사람의 풀이 참고.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        occurance = 1

# 1,1,1,2,2,3
# 1,1,2,2,3

# occur 3부터는 넘어가지 않고 pointer를 그대로 둔다.
# 그리고 다음 요소 시작할때, 그때 하나씩 옮겨준다. 

# 그러니까 3번째 요소부터는, 옮기는게 아니라 그대로 놔두고,
# 다시 새로운 요소가 시작될때 한칸씩 옮겨준다고 생각하면 된다. 이게 투 포인터;

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                occurance += 1
            else:
                occurance = 1

            if occurance <= 2:
                nums[index] = nums[i]
                index += 1
        
        return index
        

# 10:21 시작. 25분. 1차시도 실패.

# 0. 오른쪽으로 쭉 돈다. 만약 cnt <= 2이면 그냥 넘어감.
# 1. 현재 2보다 더 큰 거를 발견했을때, 1111 이면 어떻게?
# 2. 1찾으면, 오른쪽으로 계속 가서, 더 큰걸 찾고, 큰거 찾으면 그걸로 바꾼다.
# 3. 그 다음 이제 그 count를 1 올리고, 다시 반복..

# 만약 2번에서 오른쪽 끝으로 갔다? 그러면..그 부분은 비워둔다. 

# 근데 이렇게 하면 문제는, 111 2 이렇게 있을때, 11 22로 바꿔버린다는 것.
# 원하는거는 11 2 이렇게 되는거고.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_num = nums[0]
        curr_cnt = 0
        should_underscore = False
        und_cnt = 0

        for i in range(len(nums)):
            flag = False

            if should_underscore:
                nums[i] = "_"
                und_cnt += 1
                continue

            if nums[i] == curr_num:
                curr_cnt += 1
            
            if curr_cnt >= 3:
                # 오른쪽으로 계속 가서, 더 큰걸 찾고, 큰거 찾으면 그걸로 바꾼다.
                # 더 큰걸 못찾고 array를 벗어났다? 그러면 그 요소부터는 전부 should_underscore.
                for j in range(i+1,len(nums)):
                    if nums[j] > curr_num:
                        curr_num = nums[j]
                        nums[i] = curr_num
                        curr_cnt = 1
                        flag = True
                        break

                # 못찾았다? 그러면 
                if not flag:
                    should_underscore = True
                    nums[i] = "_"
                    und_cnt = 1
        
        return len(nums) - und_cnt