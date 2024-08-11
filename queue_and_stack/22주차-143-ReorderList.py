# 1차시도 실패. 일단 시도는 좋은데, 
# 같은 val이 있을때의 시도를 고려하지 못함.

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr, curr_fast = head, head
        while curr.next and curr_fast and curr_fast.next:
            curr, curr_fast = curr.next, curr_fast.next.next
        
        queue = []
        
        while curr:
            queue.append(curr.val)
            curr = curr.next
        
        if curr_fast:
            queue.pop(0)

        curr = head
        while curr:
            temp = curr.next
            # 이 부분에서 문제를 일으킨 것.
            if queue and temp.val == queue[-1]:
                temp.next = None
                break
            if not queue:
                curr.next = None
                break
            newNode = ListNode(queue.pop())
            curr.next = newNode
            newNode.next = temp
            curr = temp