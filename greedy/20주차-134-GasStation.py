# 1차시도. 시간초과. 브루트 포스로 풀었는데.

# cost 3 4 5 1 2
# gas  2 3 4 5 1

# cost 3 4 3 
# gas  3 4 2

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def get_idx(curr,arr):
            return curr if curr < len(arr) else curr - len(arr)
        
        gas[:] = gas[1:] + gas[:1]
        cand = []
        
        for i in range(len(gas)):
            if gas[i] >= cost[get_idx(i+1,gas)]:
                cand.append(i)

        res = -1
        for idx in cand:
            start = gas[idx]
            flag = True
            for dx in range(1,len(gas)+1):
                start -= cost[get_idx(idx+dx,gas)] 
                if start < 0:
                    flag = False
                start += gas[get_idx(idx+dx,gas)]
            if flag:
                res = idx + 1

        return get_idx(res,gas)
    
# 2차시도. 풀이 참고.
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas, total_cost, start, curr_tank = 0, 0, 0, 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            # 나랑 달랐던 부분은, 이 사람은 그 다음것도 갈 거를 미리 예상하고 그걸 갈 수 없는지를 gas[i] - cost[i]로 판단한다는 것이다.
            # 여기서 0이면 그냥 주저앉으면 되는 거니까.
            
            curr_tank += gas[i] - cost[i]
            
            # ***여기가 핵심이다.
            # 근데 만약 i=1에서 주저앉았다. 그러면 start =0은 안되네.. 그러면 start = 1부터 가야 하는거 아니야?
            # 생각해봐. 어쨌거나 이전 시점에서으 curr_tank는 0보다 클 건데, 그 start 시점에서 gas-cost가 안된다고 한다면
            # 그 start 시점보다 한칸 더 크든 두칸 더 크든 의미가 없다는 것이다. 왜냐면 그 전 시점에서는 0보다 컸었는데도 안되었으니까.

            # 뭔가 dp스럽기도 하고. 중복계산을 피해주기 위해서는, 결국 논리적으로 이거는 안해도 된다..라는 것을.

            # 글면 start = i+1에서는 왜 len(gas)-1까지만 봐주면 되는걸까?
            # 
            if curr_tank < 0: 
                start = i + 1
                curr_tank = 0
        
        if total_gas < total_cost:
            return -1
        else:
            return start
