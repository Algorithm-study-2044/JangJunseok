# 1차시도. 막힘.

class Solution(object):
    def shortestPathLength(self, graph):    
        path = [[0]*len(graph)]
        for i in range(len(graph)):
            for item in graph[i]:
                path[i][item] = 1
        
        # 이렇게 하면 이차원 배열이 완성이 됨.
        visited = [False] * len(graph)

        def find_not_visited(visited):

            for i in range(len(visited)):
                if not visited[i]:
                    print("dfdf")

        for i in range(len(graph)):
            for j in graph[i]:
                # 1을 방문하고, 그 인접지역을 방문하고.
                # 그러면 또 포문을 써야하는건가?
                print("dfd")


# 2차시도. 다른 사람의 풀이 연구. 근데 잘 모르겠다. ㅋㅋㅋ

class Solution:
  def shortestPathLength(self, graph: List[List[int]]) -> int:
    n, success = len(graph), (1 << len(graph)) - 1
    if n == 1:
      return 0

    seen = [[0] * (1 << n) for _ in range(n)]
    frontier, steps = [], 0
    for node in range(n):
      frontier.append((node, 1 << node))
      seen[node][1 << node] = 1

    # frontier에는 각 노드와, 해당 노드만큼의 2의 제곱 비트가 들어갈 것임.

    # 예를 들어 봅시다. 0의 경우 [1,2,3]인데, 

    # 그러면 1방문하고 mask씌우고, 2방문하고 mask씌우고, 3방문하고 mask씌우고,
    # 그 다음에 해당 노드에서, 해당 조합이 0이라면, 1 추가해준다.
    
    while frontier:
      new_frontier = []
      for node, mask in frontier:
        for neighbor in graph[node]:
          # 현재 방문한 지역에다가, neighbor의 지역을 mask한다. 
          # 무슨말일까? 어찌보면, 모든 지역을 다 방문했다는 의미 아닐까?
          next_mask = mask | (1 << neighbor)
          # 만약 success까지 왔다? 그러면 return steps + 1 해준다. 이게 이제 정답이라는 말.
          # 지금 current까지는 steps+1이 안되어있으니까. 
          # 근데 왜 success는 len(n-1이 되는걸까.
          if next_mask == success:
            return steps + 1

          # 해당 노드에서, 뭐뭐뭐 방문했는지의 조합이 없다면, 추가해준다.
          # 그리고 그걸 new frontier에다가 넣어준다.
          if seen[neighbor][next_mask] == 0:
            seen[neighbor][next_mask] = 1
            new_frontier.append((neighbor, next_mask))
        #그거를 모든 frontier에 대해서 반복해준다. 원래 froniter에는 0뿐만 아니라, 1,2,3 노드도 있었을 테니까.
      
      steps += 1
      frontier = new_frontier

    return steps