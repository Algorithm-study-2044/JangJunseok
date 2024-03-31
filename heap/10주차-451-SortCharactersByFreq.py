# 6:11분. 9분 소요. 73ms. 17.12% beats.

from collections import defaultdict

class Solution(object):
    def frequencySort(self, s):
        #1. 한번 돌면서 freq를 체크
        #2. 다음 push할때, freq를 같이.
        #3. 그걸 join.

        freq = defaultdict(int)
        heap = []
        
        for char in s:
            freq[char] += 1
        
        for char in s:
            heap.append((-freq[char],char))
        
        heap.sort()

        return "".join([item[1] for item in heap])
    

# 2차시도. 다른사람의 풀이 연구.
    

# counter에서, 가장 빈도수가 높은 친구부터 꺼낸다. 
# 그 친구를 빈도수만큼. 곱해서 res에 더한다.
# 그리고, d에서 그 친구를 제거한다.

class Solution(object):
    def frequencySort(self, s):
        l=set(s)
        d={}
        res=''
        for i in l:
            d[i]=s.count(i)
        #sorted_d=dict(sorted(d.items()))
        keys=list(d.keys())
        val=list(d.values())
        # print(sorted_d)
        # print(keys)
        # print(val)
        while d:
            max_c=max(val)
            max_ind=keys[val.index(max_c)]
            #for _ in range(max_c):
            res+=max_ind*max_c
            d.pop(max_ind)
            keys.remove(max_ind)
            val.remove(max_c)
        return res
    

# 3차시도. 다른사람의 풀이 연구.
# freq의 key들만 sort한다음에, 그 key들을 freq[key]만큼 곱해서 res에 더한다.
    
class Solution(object):
    def frequencySort(self, s):

        # Step 1: Count the frequency of each character
        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        # Step 2: Sort the characters based on their frequencies
        sorted_chars = sorted(char_freq.keys(), key=lambda x: char_freq[x], reverse=True)
        
        # Step 3: Reconstruct the sorted string
        sorted_string = ''
        for char in sorted_chars:
            sorted_string += char * char_freq[char]
        
        return sorted_string