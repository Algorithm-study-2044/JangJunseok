#1차시도. 실패. 이렇게 하면 트리가 떨어져있을때 하나인지 아닌지를 판단을 못해서
#union parent 방식을 활용하려고 했지만..
#그러면 루트노드가 여러개일때, 모든 루트노드는 같아야 함.

from collections import defaultdict

class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        visited = [False] * n
        visited[0] = True
        self.parent = {}

        for i in range(n):
            left = leftChild[i]
            right = rightChild[i]
            self.parent[i] = i
            
            if left != -1:
                if not visited[left]:
                    visited[left] = True
                    self.parent[left] = i
                    
                else:
                    return False
        
            if right != -1:
                if not visited[right]:
                    visited[right] = True
                    self.parent[right] = i
                else:
                    return False
                
        return True
            
        
    def find_parent(self,node):
        if self.parent[node] != node:
            return self.find_parent(self.parent[node])
        return node
    
    def union_parent(self, left, right):
        left_p = self.find_parent(left)
        right_p = self.find_parent(right)

        if left_p < right_p:
            parent[right_p] = left_p
        elif left_p > right_p:
            parent[left_p] = right_p

#2차시도. 다른 사람의 풀이 참고. 
# 모두 연결되어 있다는 것을 어떻게 알 수 있나? 

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
        
        #여기까지 하면? temp에는 루트노드가 들어있을 것이다.

        if(len(temp)!=1):
            return False

        for key in temp.keys():
            root = key

        def dfs(node):
            #만약에 지금 탐구하는 node가 이미 방문한 노드라면, false를 return한다.
            if(node in visited):
                return False
            ans = True
            visited[node] = 1
            for child in graph[node]:
                ans = ans and dfs(child)
            return ans

        visited = {}
        ans = dfs(root)

        
        if(ans and len(visited)==n):
            return True
        return False
    

# 3차시도. 다른사람의 풀이 연구. 
    
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent={}
        for p,child in enumerate(zip(leftChild,rightChild)):
            for c in child:
                if c==-1:
                    continue 

                # 이미 방문한것. 이러면 안된다.
                if c in parent:
                    return False 
                
                # 만약 0 -> 1 인데, 0이 있고, 1 -> 0 일때는 안된다.
                if p in parent and parent[p]==c:
                    return False 
                
                # 모든 경우에 해당이 안되면 등록.
                parent[c]=p

        # 전체에서 자식나온거 다 빼면, 루트노드가 나올것임. 그 어떤 부모에 의해서도 등록되지 않은 친구들.
        root=set(range(n))-set(parent.keys())

        # 이러면 연결되어 있는 그래프가 여러개가 있다는 것이어서. 안되고.
        if  len(root)!=1:
            return False
        
     
        # 밑에 있는 거는 왜 해주어야 하나? rootNOde는 하나인데, 뭉텡이가 여러개인 경우가 있을 수 있음.
        # 왜? 한 뭉텡이가 rootNode가 아닌 경우가 그러함.
        def count(root):
            if root ==-1:
                return 0
            return  1+count(leftChild[root])+count(rightChild[root])
        return count(root.pop())==n