class Solution(object):
    def gcd(self, a, b):
        # Function to compute the greatest common divisor (GCD) using the Euclidean algorithm
        while b:
            a, b = b, a % b  # Update a to b and b to a % b until b becomes 0
        return a  # Return the GCD

    def insertGreatestCommonDivisors(self, head):
        # Function to insert GCDs between nodes in a linked list
        ans = ListNode(0)  # Create a dummy node to help build the new list
        cur = ans  # Pointer to the last node in the new list

        # Loop through the original linked list until the second last node
        while head.next:
            gcd_val = self.gcd(head.val, head.next.val)  # Calculate GCD of the current and next node values
            
            cur.next = ListNode(head.val)  # Create a new node for the current node's value
            cur.next.next = ListNode(gcd_val)  # Create a new node for the GCD value
            
            head = head.next  # Move to the next node in the original list
            cur = cur.next.next  # Move to the last node in the new list (the newly added GCD node)

        cur.next = ListNode(head.val)  # After exiting the loop, add the last node's value
        
        return ans.next  # Return the new list starting from the first actual node (skipping the dummy node)

# 8:22 시작. 15분 소요. 347ms. 12.28% beats.

# 최대공약수 구했다고 가정하고
# while curr and curr.next:
# next를 temp에 넣고, 공약수로 노드만들고 next에 넣어주고,
# 노드의 next는 temp. 그 다음에 curr는 temp로.

# 최대공약수는 어떻게 구하나?
# 18과 6이 있을때.
# 단순하게 보면 그냥 1부터? ㅎㅎ
# 아니면 이진탐색으로 logN까지 줄인다.
# 이게 안된다. 왜냐하면 이진탐색은 정렬이 되어있으어야 하는데,
# 약수 찾기는 1에서 6까지라고 할때 되는게 있고 안되는게 있으니까.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        def get_gcd(n1,n2):
            if n1 < n2:
                n1,n2 = n2,n1
            for i in range(n2,-1,-1):
                if n1 % i == 0 and n2 % i == 0:
                    return i
                
        curr = head
        while curr and curr.next:
            temp = curr.next
            val = get_gcd(curr.val,temp.val)
            newNode = ListNode(val,temp)
            curr.next = newNode
            curr = temp                       
        
        return head  