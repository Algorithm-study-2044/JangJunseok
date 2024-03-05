#6주차. 이렇게 하니까 시간 초과가 떴음. 애초에 스터디에서 소개한 방법과 어떻게 다르지>?

class Solution(object):

    def findRoot(self,a):
        if self.map[a] == a:
            return a
        else:
            return self.findRoot(self.map[a])

    def union_parent(self,a,b):
        aRoot = self.findRoot(a)
        bRoot = self.findRoot(b)

        if aRoot > bRoot:
            self.map[b] = aRoot
            fromVal = bRoot
            toVal = aRoot
        else:
            self.map[a] = bRoot
            fromVal = aRoot
            toVal = bRoot

        for idx in range(len(self.map)):
            if self.map[idx] == fromVal:
                self.map[idx] = toVal

    def validPath(self, n, edges, source, destination):
        self.map = list(range(n))

        for a,b in edges:
            self.union_parent(a,b)
        
        if self.findRoot(source) == self.findRoot(destination):
            return True
        else:
            return False