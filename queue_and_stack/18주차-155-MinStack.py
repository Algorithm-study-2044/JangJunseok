# 59ms. 33.46% beats.
# min을 위해서, min_arr을 만들어놓고, min_arr[-1]이랑 비교해서 넣어주면 된다.

# 처음에 문제를 잘못 이해함..getmin 한다음에 뽑는게 아니었다. 그러면. 쉽지 않나?
# pop할때 그게 minValue인 경우만 좀 생각해주면 됨.

class MinStack:
    def __init__(self):
        self.map = {-1:-1}
        self.min_arr = [(float("inf"),-1)]
        self.idx = -1

    def push(self, val: int) -> None:
        self.idx += 1
        if self.min_arr[-1][0] > val:
            self.min_arr.append((val,self.idx))
        self.map[self.idx] = val    

    def pop(self) -> None:
        target = self.map[self.idx]
        del self.map[self.idx]
        if self.idx == self.min_arr[-1][1]:
            self.min_arr.pop()
        self.idx -= 1
        return target

    def top(self) -> int:
        return self.map[self.idx]

    def getMin(self) -> int:
        min_idx = self.min_arr[-1][1]
        return self.map[min_idx]
    