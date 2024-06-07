# 1치시도. 50ms. 25% beats.
#일단 이렇게 해도 되지만, 다른 방식으로도 판별해볼것.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        
        return False
    
# 다른 방식.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True

        return False