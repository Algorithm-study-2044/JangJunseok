# 10:45 시작. 15분 소요. 425ms. 10.49% beats.
# 시간복잡도가 좀 낮게 나오기는 하다.

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        self.prev = None
        self.recent = None
        self.first = None

        self.idx = 0
        self.min_dist = float("inf")
        self.max_dist = -1

        def DFS(node):
            if not node:
                return

            self.idx += 1

            if self.prev and node.next:
                if (self.prev < node.val and node.next.val < node.val) or (self.prev > node.val and node.next.val > node.val):
                    if not self.first:
                        self.first = self.idx                    
                    else:
                        self.min_dist = min(self.min_dist, self.idx - self.recent)
                        self.max_dist = max(self.max_dist, self.idx - self.first)
                    
                    self.recent = self.idx

            self.prev = node.val

            DFS(node.next)

        DFS(head)

        if self.min_dist == float("inf"):
            self.min_dist = -1

        return [self.min_dist, self.max_dist]

# 다른 사람의 풀이. 그냥 내가 처음 생각한대로 그런 점들의 idx를 다 저장한다음에 한번 재귀하면 되는 문제였다.
# 근데 나는 그걸 한번 더 도는게 싫어서 매번 업데이트해줬던 거고.

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        critical_points = []
        prev = head
        curr = head.next
        position = 1

        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                critical_points.append(position)
            prev = curr
            curr = curr.next
            position += 1

        if len(critical_points) < 2:
            return [-1, -1]

        min_distance = float('inf')
        max_distance = critical_points[-1] - critical_points[0]

        for i in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[i] - critical_points[i - 1])

        return [min_distance, max_distance]
        