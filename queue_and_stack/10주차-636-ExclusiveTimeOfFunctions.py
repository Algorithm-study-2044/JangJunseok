# 2차시도. 성공. 30분 소요. 59ms. 54% beats.

# 자잘한 거지만, n을 알기에 그냥 [0] * n으로 초기화해줘도 된다.

from collections import defaultdict

class Solution(object):
    def exclusiveTime(self, n, logs):

        call_stack = []
        count_dict = [0] * n
        curr_time = 0
        curr_type = None

        for i in range(len(logs)):
            #들어오는애
            id, typeOfTime, timestamp = logs[i].split(":")
            id = int(id)
            timestamp = int(timestamp)
            #기존에 있던 애
            if not call_stack:
                call_stack.append((id,typeOfTime,timestamp))
                continue

            curr_id, curr_typeOfTime, curr_timestamp = call_stack[-1]
            curr_id = int(curr_id)
            curr_timestamp = int(curr_timestamp)
        
            if curr_type == "end":
                curr_time += 1

            # start가 더 들어오는 경우.
            if (id == curr_id and typeOfTime == curr_typeOfTime) or (id != curr_id):
                count_dict[curr_id] += (timestamp - curr_time)
                call_stack.append((id,typeOfTime,timestamp))

            #이 경우 짝이 맞는것이다. 
            else:
                count_dict[id] += (timestamp - curr_time + 1)
                call_stack.pop()
            
            curr_time = timestamp
            curr_type = typeOfTime

        return count_dict

# 3차시도. 다른 사람의 풀이 연구.
    
# 내 경우는 같은 함수 재귀호출, 짝이 맞을때, start가 계속 들어올때. 

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        stack, ans = deque(), [0]*n                         # Example: ["0:start:0", "0:start:2", "0:end:5",
                                                            #           "1:start:6", "1:end  :6", "0:end:7"]
    
        for log in logs:                                    #                time-
            id, action, timestamp = log.split(":")          #   id   action  stamp    ans    stack
            id, timestamp = int(id), int(timestamp)         #  ––––   ––––    ––––   –––––   –––––––––
                                                            #    0    start     0    [0,0]   [(0,0)]
            if action == "start":                           #    0    start     2    [0,0]   [(0,0),(0,2)]
                stack.append((id, timestamp))               #    0     end      5    [0,0]   [(0,0)]
                                                            #    1    start     6    [0,0]   [(0,0),(1,6)]
            else:                                           #    1     end      6    [0,1]   [(0,0)]
                id, initTime = stack.pop()                  #    0     end      7    [7,1]   []
                elapsedTime = timestamp + 1 - initTime
                ans[id]+= elapsedTime

                #마지막에 남아있는 친구는 startTime과 endTIme의 차이만큼 빼면 너무 많이 빼게 된다.
                #elapsedTime만큼은 일을 못하게 되어버린 거니까.
                if stack: ans[stack[-1][0]]-= elapsedTime
               
        return ans




# 1차시도. 실패. 시간초과.

from collections import defaultdict

class Solution(object):
    def longestConsecutive(self, nums):

        #해당 -으로 시작하는 가장 긴 length
        self.dp = defaultdict(int)
        #방문했는지 안했는지를 기록.
        self.hm = defaultdict(list)
        #4가 있는데 5가 들어왔다? 그러면 dp의 4를 업데이트해줘야 함.
        #4가 있는데 3이 들어왔따?

        
        # 2 1 3 이 순서대로 들어왔다고 하자.
        # dp[2] = 1, hm[1] = [2]
        # hm에 있네. 그러면 해당 value를 타고 가서 dp를 업데이트.
        # dp[2] = 2 이렇게 되고, dp[1] = 1이렇게 되고, hm[1] = 0, hm[3] = 2
        # 그 다음 3이 들어오면? hm[3] = 2이니까 . dp[2] = 3으로 업데이트,.

        # 3 2 4 이렇게 들어오면?
        # 3 입장에서는 2나 4있으면 올라감. 

        # 그러면 2나 4를 등록해놓고
        # 2가 들어왔다? 그러면 이제 dp[3] += 1
        # 이제는 trigger가 2 4 가 아니라 1 4 가 되는거임.
        # 그러면 hm[2] = 3 이 아니라, hm[1] = 3으로 바꿔줘야함.



        for item in nums:
            self.hm[item-1] = item
            if item+1 not in self.hm:
                self.hm[item+1] = item
            
            self.hm[item+1] = item
            if item in self.hm:
                triggered = self.hm[item]
                self.dp[triggered] += 1
                self.hm[item-1] = triggered
                    
        return max(self.dp.values())