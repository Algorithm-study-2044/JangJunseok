# 4주차. 실패. 1. orderedDict를 사용한 풀이.

from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = OrderedDict()
        """
        :type capacity: int
        """
        

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.cap:
                self.cache.popitem(last=False)
            self.cache[key] = value


# 2. 연결리스트를 사용한 풀이. 702ms. 94% beats.

# value 업데이트 할때도 우선순위에 넣어야 한다.
# 그리고 새롭게 put할때도, 우선순위에 들어간다. 이거는 문제에 나와있나??     

# 우선순위 업데이트를 힙을 사용하던지, 아니면 연결리스트로 구현하던지.
# 근데 힙을 사용하면, 우선순위 업데이트가 어렵다. 힙에서 맨 왼쪽만 뺄 수 있으니까.
# 그래서 해쉬맵을 사용해서, 해당 node의 value 값을 구할 수 있도록 하면서도,
# 그 순위를 업데이트할 수 있도록 하는 자료구조가 필요한 것이다.       

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None# tail -> cache에서 제거할때, 

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity    
        self.hm = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)   
        self.head.next = self.tail
        self.tail.prev = self.head  

    def get(self, key): 
        if key in self.hm:
            node = self.hm[key]
            ans = node.value
            self.deleteNode(node)
            self.addNode(self.head,node)
            return ans
        return -1
    
    def deleteNode(self,node):
        node_before = node.prev
        node_after = node.next
        node_before.next = node_after
        node_after.prev = node_before
        node.prev = None
        node.next = None

    def addNode(self,target,node):
        head_nnext = target.next
        target.next = node
        node.prev = target
        node.next = head_nnext
        head_nnext.prev = node

    def put(self, key, value):
        if key in self.hm:
            node = self.hm[key]
            node.value = value
            self.deleteNode(node)
            self.addNode(self.head, node)
        else:
            # 이러면 하나 빼야함.
            if len(self.hm) == self.capacity:
                del self.hm[self.tail.prev.key]
                self.deleteNode(self.tail.prev)
                newNode = Node(key,value)
                self.hm[key] = newNode
                self.addNode(self.head, newNode)
            # 하나 빼지 않고, 그냥 넣으면 됨.
            else:
                newNode = Node(key,value)
                self.hm[key] = newNode
                self.addNode(self.head, newNode) 
