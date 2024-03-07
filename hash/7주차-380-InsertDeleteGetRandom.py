# 7주차. 2차시도. 다른사람의 풀이연구. 

    # remove가 가장 궁금했다. 기본적으로 delete 하게 되면, self.lst에서 그 값을 pop해야하니까 시간복잡도가 O(1)이 아니게 되지 않나?
    # 그런데 뒤에 있는 값을 앞으로 덮어씌워주면, pop을 해도 되는 것이다. 그리고 그때, self.idx_map에서도 해당 값을 지워줘야한다.
    # 어차피 self.lst에서 중요한것은 값이 있냐만 

import random

class RandomizedSet(object):

    def __init__(self):
        self.arr = []
        self.idx_map = {}

    def insert(self, val):
        if val in self.idx_map:
            return False
        
        self.arr.append(val)
        self.idx_map[val] = len(self.arr) -1
        return True

    def remove(self, val):
        if val not in self.idx_map:
            return False
        
        target_index = self.idx_map[val]
        last_value = self.arr[-1]
        self.arr[target_index] = last_value
        self.idx_map[last_value] = target_index
        self.arr.pop()
        del self.idx_map[val]
        return True

    def getRandom(self):
        return random.choice(self.arr)
        """
        :rtype: int
        """
