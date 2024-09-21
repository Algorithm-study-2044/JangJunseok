# 2차시도. 185ms. 53.8% beats.

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        prov = [1 for i in range(n)]

        def DFS(i):
            for idx,val in enumerate(isConnected[i]):
                if idx != i and val == 1 and prov[idx] == 1:
                    prov[idx] = 0
                    DFS(idx)
        
        cnt = 0
        for idx,val in enumerate(prov):
            if val == 1:
                cnt += 1
                DFS(idx)

        return cnt
    


# 1차시도.

# union_find를 통해서, 자식을 다 통합시켜주면 어떨까 싶은데?

# 이렇게 union하면 안되는게, 
# 봐봐..만약에 1-2 2-3 이렇게 연결되어 있다면,
# 결국에는 1의 부모는 2로 남아버리겠지.

# 즉 dfs를 통해서 1-2 연결하고, 2-3 연결하면, 2를 타고 가서, 
# 1-2 2-3 이렇게 있다면. 3-5

# 0부터 시작해서, 연결된 애들을 다 바꿔주면 되는거 아닌가?
# 0연결된 애들 다 0으로
# 그 다음 1 들어가서 1과 연결된 애들 다 바꿔주고,

# 가장 큰 놈부터 시작? 그래서 그 밑에놈이 갔을때, 이미 그것보다 크다면 바꿔줄 필요가 없다.

# 3 -> 2의 부모 3으로 바꿈.
# 2 1 이렇게 되면,