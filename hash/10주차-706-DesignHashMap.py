#1차시도. 254ms. 22.9% beats.

class MyHashMap:

    def __init__(self):
        self.hm = [-1] * (10**6)

    def put(self, key: int, value: int) -> None:
        hashed_key = key % (10**6)
        self.hm[hashed_key] = value

    def get(self, key: int) -> int:
        return self.hm[key%(10**6)]
        

    def remove(self, key: int) -> None:
        self.hm[key%(10**6)] = -1


# 2차시도. 

class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []
        

    def put(self, key: int, value: int) -> None:
        try:
            idx = self.keys.index(key)
            self.values[idx] = value
        except:
            #새로 넣어야 함.
            self.keys.append(key)
            self.values.append(value)

    def get(self, key: int) -> int:
        try:
            idx = self.keys.index(key)
            return self.values[idx]
        except:
            return -1

    def remove(self, key: int) -> None:
        try:
            idx = self.keys.index(key)
            del self.keys[idx]
            del self.values[idx]
        except:
            pass

        