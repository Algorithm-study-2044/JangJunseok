#4주차. List가 아니라 이게 class 인스턴스가 들어있는거다. 다시풀어볼것.

class NestedIterator(object):

    def __init__(self, nestedList):

        self.curr_list = nestedList
        self.before_list = None
        self.depth = 0  
        self.stack = []
        self.idx = 0

    def next(self):
        self.curr_obj = self.curr_list[self.idx]
        res = None

        if self.curr_obj.isInteger():
            self.idx += 1
            res = self.curr_obj.getInteger()
        else:
            # 안쪽 리스트로 들어가야함.
            self.depth += 1
            self.stack.append(self.idx)
            self.before_list = self.curr_list
            self.curr_list = self.curr_obj.getList()
            self.idx = 0
            res = self.curr_list[self.idx]

        if self.idx == len(self.curr_list):
            self.curr_list = self.before_list
            self.idx = self.stack.pop()
            self.depth -= 1
        
        return res


    def hasNext(self):
        if self.depth == 0 and self.idx == len(self.curr_list) - 1:
            return False
        else:
            return True
        

#4주차. 2차시도. 다른 사람의 풀이 연구.
#재귀의 개념을 잘 이해할것.
    
class NestedIterator:
    def __init__(self, nestedList):
        def flatten(nl):
            ans=[]
            for i in nl:
                if i.isInteger():
                    ans.append(i.getInteger())
                else:
                    ans.extend(flatten(i.getList()))    
            return ans
        self.n=deque(flatten(nestedList))            
    
    def next(self) -> int:
        return self.n.popleft()
    
    def hasNext(self) -> bool:
         return self.n
    
# 다른 사람의 풀이. 마찬가지로 재귀를 활용했음.
class NestedIterator:
    def __init__(self, nestedList):
        # The list of NestedInteger elements to be flattened
        self.nestedList = nestedList
        
        # The flattened list of integers
        self.flattenedList = []
        
        # Index to keep track of the current position in the flattenedList
        self.currentIndex = 0

        # Recursively flattens the nested list and adds integers to the flattenedList
        def flatten(currentList):
            for item in currentList:
                if item.isInteger():
                    self.flattenedList.append(item.getInteger())
                else:
                    # Recursively flatten nested lists
                    flatten(item.getList())
        
        # Flatten the nestedList during initialization
        flatten(self.nestedList)

    # Returns the next integer in the flattened list
    def next(self):
        number = self.flattenedList[self.currentIndex]
        self.currentIndex += 1
        return number
