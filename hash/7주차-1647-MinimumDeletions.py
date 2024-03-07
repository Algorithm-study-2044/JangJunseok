#7주차. 25분 소요. 511ms. 5.31% beats.

class Solution(object):
    def minDeletions(self, s):

        table = {}
        didCome = {}

        for item in s:
            if item not in didCome:
                didCome[item] = 1
                if 1 not in table:
                    table[1] = 1
                else:
                    table[1] += 1
            else:
                #item이 didCome에 있었을때
                didCome[item] += 1
                table[didCome[item]-1] -= 1
                if didCome[item] in table:
                    table[didCome[item]] += 1 
                else:
                    table[didCome[item]] = 1
        
        curr = 0
        res = 0
        for vals in reversed(table.values()):
            if vals + curr > 1:
                res += (vals + curr - 1)
                curr += (vals - 1)
            else:
                curr = 0

        return res
    

# 다른 사람의 풀이 연구.
    
# Counter를 사용해서 간단하게 파악할 수 있다.
    
# 그리고, 중복되는 frequencies가 있을때, 그것을 없애주기 위해서 -1 해주는 방식을 사용했다.

class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        deletions = 0
        used_frequencies = set()
        
        for char, freq in cnt.items():
            while freq > 0 and freq in used_frequencies:
                freq -= 1
                deletions += 1
            used_frequencies.add(freq)
            
        return deletions