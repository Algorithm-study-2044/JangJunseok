# 이진트리의 개념 자체를 헷갈렸음.
# 단일루트노드, 사이클없음. 각노드는 하나의 부모만,

from collections import defaultdict
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = defaultdict(list)
        temp = {}
        for i in range(n):
            temp[i] = 1

        for i in range(n):
            if(leftChild[i]!=-1):
                graph[i].append(leftChild[i])
                if(leftChild[i] in temp):
                    del temp[leftChild[i]]
            if(rightChild[i]!=-1):
                graph[i].append(rightChild[i])
                if(rightChild[i] in temp):
                    del temp[rightChild[i]]

        # 단일 루트노드가 존재하지 않으면 return False.
        if(len(temp)!=1):
            return False

        # 그 단일 루트노드를 찾는다.
        for key in temp.keys():
            root = key

        def dfs(node):
            # 각 노드는 하나의 부모만 가져야 함.
            if(node in visited):
                return False
            ans = True
            visited[node] = 1
            for child in graph[node]:
                ans = ans and dfs(child)
            return ans

        visited = {}
        ans = dfs(root)
        
        # 모든 노드가 연결되어 있어야 함.
        if(ans and len(visited)==n):
            return True
        return False

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        # 0,1이 서로를 가리키는 상황은 어떻게 할 건지?
        def DFS(idx):
            if idx == -1:
                return True

            left = leftChild[idx]
            right = rightChild[idx]

            print(idx,left,right)

            lv = DFS(left)
            rv = DFS(right)

            if not lv or not rv:
                return False

            # 둘 중 하나가 -1인 경우는?
            if right == -1:
                return True
            
            # lv rv는 다 true다. 그러면
            if left < idx and idx < right:
                return True

            return False
        
        return DFS(0)