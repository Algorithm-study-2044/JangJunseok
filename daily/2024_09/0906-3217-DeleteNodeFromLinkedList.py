# 13분 소요. 751ms. 22.72% beats.

# nums를 hash로 만든다.
# hash에 없으면 이전 노드에서 이 노드를 건너띄고 다음 노드로,
# 반복. hash에 있는거 발견하면, prev의 next를 이 노드로 하고,

# 이 노드의 다음을 head로 넣고, 
# prev = None이면 pass, prev가 있으면 저장.
# hash에 있으면 prev에 넣고, 

# 그러면 마지막이 지워질 노드라고 한다면?
# 거기에 대한 처리도 해줘야 할듯.
# if head.next = None:

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        dels = set(nums)
        prev = None
        first = None
        while head:
            if head.val in dels:
                if not head.next:
                    prev.next = None
            else:
                if not first:
                    first = head
                if prev:
                    prev.next = head
                prev = head

            head = head.next   
        
        return first
