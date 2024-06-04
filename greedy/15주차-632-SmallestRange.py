# 1차시도. 실패. 다른 사람의 풀이 참고.
# 내가 조금 잘못 이해한 부분도 있다. 굳이 마지막까지 안해줘도. 사실 처음 시작은, 가장 작은 처음과 가장 큰 처음을 보수적으로 잡고 시작해도 되는 것.

from collections import defaultdict
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        temp = []
        for i, arr in enumerate(nums):
            for n in arr:
                temp.append((n, i))

        temp.sort()

        k = len(nums)
        # 여기까지는 뭐. 정렬한다음에, 가장 처음과 가장 끝의 처음, 즉 가장 보수적으로 잡았을때의 넓이인거고.
        ans = (temp[0][0], temp[-1][0])
        best = temp[-1][0] - temp[0][0]

        seen = defaultdict(int)
        start = 0

        # 그 다음 해야할것은 뭔가? start를 한칸 씩 뒤로 밀어보면서, k개의 영역을 다 포함하고 있는지 확인하는거다.
        # 그거를 이제 seen이라는 defaultdict로 확인하고 있는 거고.

        # 끝부분은 어디까지 밀면 되냐면. k개의 영역을 다 포함하고 있는 순간 멈춰버리면 된다.
        # 시작부분은, 

        # 궁금한건, a파트에서 b파트로 페이즈가 넘어갔을때, 
        # 다시 b파트에서 a파트로 넘어가면 그 이후에 다시 b파트로 가버리는 상황이 생길 수 있나?

        for i, (x, idx) in enumerate(temp):
            seen[idx] += 1
            if i == 0:
                continue
            
            # 5개 영역이 다 나오지 않았다면, 최소값을 갱신할 필요가 없다. 
            # a 파트.
            if len(seen) < k:
                continue

            # b 파트.
            else:
                # 5개 영역이 다 나왔을때,
                while len(seen) == k:
                    # 현재까지 나온게, 처음 시작보다 더 작다? 글면 갱신.
                    if x - temp[start][0] < best:
                        best = x - temp[start][0]
                        ans = (temp[start][0], x)

                    # 그 다음에 시작점을 하나 날려본다. 만약 그래도 5개 영역이 다 있다? 
                    y = temp[start][1]
                    seen[y] -= 1
                    if seen[y] == 0:
                        del seen[y]

                    # start+=1 한다음에 중요한게 뭔가? 
                    # 여전히 k개의 영역을 다 포함하고 있는가? 이걸 확인해야. 만약 포함하고 있는거면. 더 밀어보고.
                    start += 1

        return ans
    
# 2차시도. heap을 사용한 풀이.

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap=[]
        maxvalue=0
        for i in range(len(nums)):
            heapq.heappush(heap,[nums[i][0],i,0])
            maxvalue=max(maxvalue,nums[i][0])
        answer=[heap[0][0],maxvalue]

        # 어쨌거나 여기서 해주고 있는건, 시작지점이 가장 작은놈부터 뽑아서 한칸씩 뒤로 밀어보는거다.
        # 끝지점을 생각해줄 필요가 없는것이다. 그런데 이렇게 계속 계속 밀다가, 어느 하나라도 끝에 도달해버리면 그때는 끝내야 하는것임. 
        # 이게 핵심인듯.

        # 그리고 maxVal이 업데이트 될 수도 있다. 왜냐하면 작은놈이 뒤로 밀리면서, 제일 컸던 놈보다 커질 수 있기 때문이다.

        while True:
            _,row,col=heapq.heappop(heap)
            # 앞선 풀이에서는, seen을 가지고 생각했었는데 여기서는 이렇게 해주고 있네.
            if col==len(nums[row])-1:
                break
            next_num=nums[row][col+1]
            heapq.heappush(heap,[next_num,row,col+1])
            
            # maxValue를 갱신해주는 부분. 왜? 
            
            maxvalue=max(maxvalue,next_num)
            if maxvalue-heap[0][0]<answer[1]-answer[0]:
                answer=[heap[0][0],maxvalue]
        return answer