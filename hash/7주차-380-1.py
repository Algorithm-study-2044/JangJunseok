# 423ms. 50% beats.

import random

class RandomizedSet(object):

    def __init__(self):
        self.dic = {}

    def insert(self, val):
        if val in self.dic:
            return False
        else:
            self.dic[val] = True
            return True

    def remove(self, val):
        if val in self.dic:
            del self.dic[val]
            return True
        return False
    
    def getRandom(self):
        arr = self.dic.keys()
        rand = random.randrange(0,len(arr))
        return arr[rand]
    

# 2차시도. 다른 사람의 풀이 연구. 
# 리스트에서 찾아서 삭제하는 방법이 아니라, 리스트의 끝에 있는 값을 삭제할 값으로 덮어씌우고, 끝에 있는 값을 삭제하는 방법을 사용했다.
# index를 dict에 저장하고 있다가, 그 index를 찾아서 끝에 있는 값을 덮어씌우고, 끝에 있는 값을 삭제하는 방법을 사용했다.
# pop의 경우는 O(1)이니까.

import random

class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.idx_map = {}

    def search(self, val):
        return val in self.idx_map

    def insert(self, val):
        if self.search(val):
            return False

        self.lst.append(val)
        self.idx_map[val] = len(self.lst) - 1
        return True

    def remove(self, val):
        if not self.search(val):
            return False

        idx = self.idx_map[val]
        self.lst[idx] = self.lst[-1]
        self.idx_map[self.lst[-1]] = idx
        self.lst.pop()
        del self.idx_map[val]
        return True

    def getRandom(self):
        return random.choice(self.lst)
    

# 3차시도. 다른 사람의 풀이 연구.

class RandomizedSet:
    def __init__(self):
        self.a, self.d = [], {}


    def insert(self, v: int) -> bool:
        if v in self.d:
            return False

        self.d[v] = len(self.a)
        self.a.append(v)

        return True
        

    def remove(self, v: int) -> bool:
        if v not in self.d:
            return False

        e, i = self.a.pop(), self.d.pop(v)

        # 만약에 삭제하려는 값이 마지막 값이면, 그냥 pop만 해주면 된다!
        # e == v 이기 때문에.

        if i < len(self.a):
            self.a[i], self.d[e] = e, i
        
        return True
        

    def getRandom(self) -> int:
        return choice(self.a)

