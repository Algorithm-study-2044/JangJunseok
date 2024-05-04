#1:11. 286ms. 29% beats.
# 원리는 유사하나, 결국 a in b를 hash, dict로 사용하면 간단하다는 원리를 활용한건데,
# sort를 하니까, 더 많은 시간이 걸려버림.

# 그냥 sort 없이 가능할까?

class Solution(object):
    def minDeletions(self, s):
        c = Counter(s)
        freq_dict = {}
        freq = c.values()
        freq.sort()

        for item in freq:
            freq_dict[item] = True
        cnt = 0

        for i in range(0,len(freq)-1):
            if freq[i] == freq[i+1]:
                while freq[i] in freq_dict and freq[i] > 0:
                    freq[i] -= 1
                    cnt += 1
                freq_dict[freq[i]] = True

        return cnt
    

# 이렇게 하면 문제가, 겹치는 애들 모조리 다 빼버린다.
# 처음 들어간 친구는 괜찮게 하려면, 미리 freq_dict를 만드는게 아니라,
# 이런식으로, 넣을때마다 차지하도록 해야한다는 것.
# 298ms. 15% beats. 37%까지는 나옴.

class Solution(object):
    def minDeletions(self, s):
        c = Counter(s)
        freq_dict = {}
        freq = c.values()

        cnt = 0
        for i in range(0,len(freq)):
            while freq[i] in freq_dict and freq[i] > 0:
                freq[i] -= 1
                cnt += 1
            freq_dict[freq[i]] = True

        return cnt
    

