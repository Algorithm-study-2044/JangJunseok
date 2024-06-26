#6주차. 1차시도. 30분 소요. 1869ms. 23% beats.

# 다들 비슷하게 푼 것 같다.

class Solution(object):
    def closestNodes(self, root, queries):
        arr = []

        def DFS(node):
            if not node:
                return
            arr.append(node.val)
            DFS(node.left)
            DFS(node.right)

        DFS(root)

        arr = sorted(arr)
        res = []

        def findOne(arr,target,val):
            
            l = 0
            r = len(arr) - 1
            while l<=r:
                mid = (l+r) // 2
                if arr[mid] > target:
                    r = mid - 1
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    return arr[mid]

            if val == 0:
                if l > len(arr) - 1:
                    return -1
                return arr[l]
            else:
                if r < 0:
                    return -1
                return arr[r]
        
        for item in queries:
            min = findOne(arr,item,1)
            max = findOne(arr,item,0)
            res.append([min,max])

        return res