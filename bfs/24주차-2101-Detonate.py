# 1차시도. 25분 소요. 387ms. 67% beats. DP+BFS.

# 거리 계산. 만약 반지름보다 거리가 작다? 글면 같이 터지는거고.
# 아 이게 게다가 연쇄적으로 터진다. 무슨 말인가 하면.

# 그러면 터트린다 -> 터진게 있나? queue에 넣는다.
# queue에 넣은거 빼서, 다른 안터진 bomb들 중에서 반경내인지 확인하고, 다시 터트리고, queue에 넣고,

# 근데 이것도 일일이 구해야 하나? 예를 들어서 1번부터 터트렸다고 할때, 

# 1번 터트리면, 이제 insights를 얻는다. 아 1번 터트리면 어떤 애들이 터지는구나 라는걸.
# 그럼 나중에 3번을 터트렸을때, 봤더니 1번이 있네? 그러면 dp[1] => 
# 아니 처음부터 계산해놓으면 안되는거야? 1번 터트리고, 

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        #nC2까지만 연산하면 되나? ㄴㄴ. 이거는 n**2 필요한 작업임.
        def is_direct(source,target):
            dist = math.sqrt((source[0] - target[0])**2 + (source[1]- target[1])**2)
            if dist <= source[2]:
                return True
            return False

        dp = [[] for _ in range(len(bombs))]
        
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue
                if is_direct(bombs[i],bombs[j]):
                    # 반경 이내야? 그러면 가능한놈에다가 넣는다.
                    dp[i].append(j)

        # 터진게 있으면? queue에 넣는다.
        def BFS(init_index):
            detonated = [False for _ in range(len(bombs))]
            detonated[init_index] = True
            queue = deque([init_index])
            while queue:
                curr = queue.popleft()
                for next_idx in dp[curr]:
                    if not detonated[next_idx]:
                        detonated[next_idx] = True
                        queue.append(next_idx)
            return len([item for item in detonated if item])
        
        max_bomb = 0
        for i in range(len(bombs)):
            max_bomb = max(max_bomb, BFS(i))
        return max_bomb
        
