#6주차. 1차시도. 20분 소요. 298ms. 5.51%.

from collections import deque

class Solution(object):

    def returnSumGreaterThan(self,arr,target):
        l = 0
        r = len(arr) - 1
        idx = None
        while l <= r:
            mid = (l+r) // 2 
            if arr[mid] > target:
                r = mid
            elif arr[mid] < target:
                l = mid + 1
            else:
                idx = mid
                break
        
        return sum(arr[idx+1:])

    def convertBST(self, root):
        arr = []

        def DFS(node):
            if not node:
                return
            arr.append(node.val)
            DFS(node.left)
            DFS(node.right)


        DFS(root)

        arr = sorted(arr)

        def BFS(node):
            queue = deque([node])

            while queue:
                curr = queue.popleft()

                if curr:
                    curr.val = self.returnSumGreaterThan(arr,curr.val) + curr.val
                    queue.append(curr.left)
                    queue.append(curr.right)

        BFS(root)

        return root
    


#2차시도. 다른사람의 풀이 연구. 근데 루트 기준. 루트 왼쪽이지만.
#또 다시 루트 왼쪽에서 오른쪽이 루트보다 클 수도 있지 않나? 루트 왼쪽이면
#항상 루트보다 작은건가?
#bineary search Tree가 subtree인데, 이 node들이 다 rootNode보다 작으니까 그렇겠다.
    
class Solution(object):
    sum = 0
    def convertBST(self, root):
        if not root: return None
        self.convertBST(root.right)
        self.sum += root.val
        root.val = self.sum
        self.convertBST(root.left)
        return root