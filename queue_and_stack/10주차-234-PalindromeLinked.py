#1차시도. 10분 소요. 1263ms. 5% beats. 다른 방법은 없나?

class Solution(object):

    def isPalindrome(self, head):
        self.arr = []
        if head:
            self.save_val(head)
        half = len(self.arr) // 2
        start = 0
        end = len(self.arr) -1
        for i in range(half):
            if self.arr[end-i] != self.arr[start+i]:
                return False 
        return True
        
    def save_val(self,node):
        if not node:
            return 
        self.arr.append(node.val)
        self.save_val(node.next)


# 2차시도. 다른 사람의 풀이 참조.
# 1. 런너 기법을 사용하여 중간 노드를 찾는다.
# 2. 중간 노드를 기준으로 앞부분을 뒤집는다. (reverseNode는 reverse된 순서로 연결되어있음)
# 3. 뒷부분과 앞부분을 비교한다.
        
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        reversed_node = None
        fast = slow = head  
        while fast and fast.next: 
            fast = fast.next.next
            # reversed_node has the half of head but (reversed)

            # [1,2,3]을 생각해보자. reverseNode가 None으로 시작하면
            # slow가 2에서 3으로 가면, reverseNode도 3으로, 이 다음은? 2가 되는거임.

            # reverse_node = 1 next None
            # reverse_node = 2 next 1
            # reverse_node = 3 next 2
            # slow = 3

            reversed_node, reversed_node.next, slow = slow, reversed_node, slow.next

 
            
        if fast:
            # 중간은 비교하지 않는다. reverseNode도 중간 이전까지만 reverse되어있음.
            slow = slow.next

        
        while slow:
            if slow.val != reversed_node.val:
                return False
            else:
                slow = slow.next
                reversed_node = reversed_node.next

        return True