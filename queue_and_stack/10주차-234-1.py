# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = slow
        slow = slow.next
        prev.next = None

        # 즉 이거는 노드의 연결고리를 교체해주는 작업이었던 것이다.
        while slow:
            k = slow.next
            slow.next = prev
            prev = slow
            slow = k

        slow, fast = prev, head
        while slow:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, prev = head, head, None
        # len 홀수일때는 딱 절반만큼 slow가 오고, fast는 끝까지.
        # 짝수일때는? 절반의 다음까지 오겠다. 
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next = prev
            prev = slow
            slow = slow.next
        
        # 결국 해주고 싶은것은, 노드를 뒤집는거다. 
        # 1은 6을 가리키고, 6은 4를 가리키도록.

        # 그걸 어떻게 하면 좋을까?
        # 예를 들어 1 -> 3 -> 6 이라고 할때.

        # 첫번째로 3 -> 1로 바꾸고
        # 3을 들고 있다가
        # 6으로 넘어가서, 다시 바꿔주는거다. 

        
        fast, slow = head, prev
        #마지막 비교는 이해가 간다.
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True
        