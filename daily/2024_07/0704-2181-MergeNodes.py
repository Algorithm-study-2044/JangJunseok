# 1079ms. 9% beats.

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        self.curr = 0
        self.arr = []

        def DFS(node):
            if not node:
                return
            
            if node.val:
                self.curr += node.val
            elif self.curr != 0:
                newNode = ListNode(self.curr)
                if self.arr:
                    self.arr[-1].next = newNode
                self.arr.append(newNode)
                self.curr = 0
                
            DFS(node.next)
                
        DFS(head)
        
        return self.arr[0]