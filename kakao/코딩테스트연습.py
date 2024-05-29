# 1차시도. 다른 사람의 풀이 연구.
# [필요알골력, 필요코딩력, 얻는알골력, 얻는코딩력, 드는 시간]


def solution(alp, cop, problems):
    max_alp_req, max_cop_req = [0, 0] 
    
    for problem in problems:
        max_alp_req = max(max_alp_req, problem[0])
        max_cop_req = max(max_cop_req, problem[1])
    
    # max_cop_req + 1 * max_alp_req + 1 크기의 2차원 dp 테이블을 만든다.
    # dp 인덱스에다가 얻어지는 알골력, 코딩력을 계산하기 때문에 max_alp_req 까지 인덱스가 확장되어야 함.
    dp = [[float('inf')] * (max_cop_req+1) for _ in range(max_alp_req+1)]
    
    # 그 다음, 시작점을 잡고, dp[alp][cop] = 0으로 초기화한다.
    alp = min(alp, max_alp_req) 
    cop = min(cop, max_cop_req)
    dp[alp][cop] = 0  
    
    for i in range(alp, max_alp_req+1):
        for j in range(cop, max_cop_req+1):
            if i < max_alp_req:
                # 알골력 1을 증가하는데 드는 시간은? 
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j < max_cop_req:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                # 즉 이 문제를 풀 수 있으면, 
                if i >= alp_req and j >= cop_req:
                    new_alp = min(i+alp_rwd, max_alp_req)
                    new_cop = min(j+cop_rwd, max_cop_req)
                    # 이미 해당 부분의 좌표와, 현재 공부하는 값 중에서, 어느것이 더 걸리는 시간이 적나요?
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)
                    
    return dp[max_alp_req][max_cop_req]

# 원리는, 먼저 1씩 손수 공부하도록 해서 업데이트 하고, 


def solution(alp, cop, problems):
    answer = 0
    
    target_alp, target_cop = [0,0]
    
    for i in problems:
        target_alp = max(target_alp,i[0])
        target_cop = max(target_cop,i[1])
    
    matrix = [[float("inf")] * (target_cop + 1) for _ in range(target_alp + 1)]
    
    start_alp = min(alp, target_alp)
    start_cop = min(cop, target_cop)

    matrix[start_alp][start_cop] = 0

    for i in range(start_alp, target_alp):
        for j in range(start_cop, target_cop):
            matrix[i+1][j] = min(matrix[i+1][j],matrix[i][j] + 1)
            matrix[i][j+1] = min(matrix[i][j+1],matrix[i][j] + 1)
    
    # 조건을 이렇게 수정하지 않으면 테스트케이스 하나 통과를 못함.
    # 0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]] 이건데,
    # 이거를 통과못하는 이유는.

    # 즉 i = target_alp 와 j = target_cop 일때, 

    # for i in range(start_alp, target_alp+1):
        # for j in range(start_cop, target_cop+1):
            # if i < target_alp:
                # matrix[i+1][j] = min(matrix[i+1][j],matrix[i][j] + 1)
            # if j < target_cop:
                # matrix[i][j+1] = min(matrix[i][j+1],matrix[i][j] + 1)
            
            for req_alp, req_cop, gain_alp, gain_cop, cost in problems:
                # 언제 이 문제를 풀 수 있나? 
                if req_alp <= i and req_cop <= j:
                    max_alp, max_cop = min(target_alp, i+gain_alp), min(target_cop, j+gain_cop)
                    matrix[max_alp][max_cop] = min(matrix[max_alp][max_cop], matrix[i][j] + cost)    
    
    answer = matrix[target_alp][target_cop]
    
    return answer