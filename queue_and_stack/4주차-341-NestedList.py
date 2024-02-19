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