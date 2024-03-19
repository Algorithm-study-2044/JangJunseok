#1차시도. 실패. 그래서 순환 에러가 날때 어떻게 처리해야할지 잘 모르겠었다.

class Solution(object):

    def union_parent(self,node1,node2):
        if self.find_parent(node1) >= self.find_parent(node2):
            self.node_map[node2] = self.find_parent(node1)
        else:
            self.node_map[node1] = self.find_parent(node2)

    def find_parent(self,node):
        if self.node_map[node] == node:
            return node

        return self.find_parent(self.node_map[node])

    def canFinish(self, numCourses, prerequisites):
        self.node_map = list(range(numCourses))
        for item1,item2 in prerequisites:
            self.node_map[item1] = item2

        for pre in prerequisites:
            self.node_map[pre[0]] = self.find_parent(pre[1])
        
        # TODO: 순환 연결 제거.
        print(self.node_map)
        return False
    

#2차시도. 다른 사람의 풀이 참고. 64ms. 75 beats.
    
from collections import defaultdict, deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        
        req_list = [0] * numCourses
        adj_dict = defaultdict(list)
        visited_count = 0
        
        for pre in prerequisites:
            adj_dict[pre[1]].append(pre[0])
            req_list[pre[0]] += 1

        queue = deque([])

        for index in range(len(req_list)):
            if req_list[index] == 0:
                queue.append(index)
                req_list[index] = -1
                visited_count += 1
        
        while queue:
            curr = queue.popleft()
            for target in adj_dict[curr]:
                req_list[target] -= 1
                if req_list[target] == 0:
                    queue.append(target)
                    visited_count += 1
        
        return visited_count == numCourses