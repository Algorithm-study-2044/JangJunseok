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
    

#2차시도. 다른 사람의 풀이 참고. 60ms. 90% beats.
    
from collections import deque, defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # prerequisites에 있는것들은 바로 못듣는다.
        # 그리고 pre에 없는것들은 다 들을 수 있다.
        queue = deque([])
        pre_map = defaultdict(list)
        visited = 0
        courses_pre = [0] * (numCourses)
        
        for pre in prerequisites:
            pre_map[pre[1]].append(pre[0])
            courses_pre[pre[0]] += 1
        
        initial_queue = [index for index, value in enumerate(courses_pre) if value == 0]
        queue = deque(initial_queue)

        while queue:
            curr = queue.popleft()
            visited += 1
            if curr in pre_map:
                for item in pre_map[curr]:
                    courses_pre[item] -= 1
                    if courses_pre[item] == 0:
                        queue.append(item)
        
        return visited == numCourses