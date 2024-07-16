# 2차시도. 성공. 41ms. 36.98ms. 

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        saved = {}
        curr = head

        if not head:
            return None

        def find_or_create(id,val):
            if id in saved:
                return saved[id]
            else:
                newNode = Node(val,None,None)
                saved[id] = newNode
                return newNode
        
        while curr:
            t = find_or_create(id(curr),curr.val)
            if curr.next:
                t.next = find_or_create(id(curr.next),curr.next.val)
            if curr.random:
                t.random = find_or_create(id(curr.random),curr.random.val)
            
            curr = curr.next

        return saved[id(head)]

