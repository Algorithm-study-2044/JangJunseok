# 15분 소요. 1차시도. 166ms. 95.11% beats. 

class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        self.stack = self.stack[:self.idx+1]
        self.stack.append(url)
        self.idx += 1

    def back(self, steps: int) -> str:
        go = min(self.idx,steps)
        self.idx -= go
        return self.stack[self.idx]

    def forward(self, steps: int) -> str:
        go = min(len(self.stack)-1-self.idx,steps)
        self.idx += go
        return self.stack[self.idx]