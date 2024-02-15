# 4주차. 실패. 다른사람의 풀이 연구.
# 기본적으로는 그리디다. 가장 많이 나오는 문자를 먼저 넣는다. 

# 힙에서는 언제 제거하나? 0이 나오면 제거한다. 아니, 안넣는다는게 맞겠다.
# result에다가 문자열을 삽입할때, 그 다음 삽입해야할 문자열이랑 result의 끝문자열이 같으면,


import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:

        hashm={}
        res=""
        for i in s:
            if i in hashm:
                hashm[i]+=1
            else:
                hashm[i]=1

        h=[]

        # hashMap도 기본적으로는 for문을 사용할 수 있다. 이렇게 하면 key값을 가져올 수 있다.
        for i in hashm:
            heapq.heappush(h,[-hashm[i],i])

        
        temp=heapq.heappop(h)
        res+=temp[1]
        if temp[0]+1:
            heapq.heappush(h,[temp[0]+1,temp[1]])

        # 언제까지 삽입하나? h가 비어있을때까지 삽입한다. 즉 넣어야할 문자가 더이상 없을때까지.
        while h:
            # 그 다음으로 넣어야할 문자와 다르면, 그러면 그냥 넣어도 된다.
            if res[-1]!=h[0][1]:
                temp=heapq.heappop(h)
                res+=temp[1]
                if temp[0]+1:
                    heapq.heappush(h,[temp[0]+1,temp[1]])
            # 그런데 그 다음으로 넣어야할 문자와 같으면?? 그러면 빼서 넣으면 안된다. 중복되어버리기 때문이다.
            # 그러면 어떻게? 문자를 두개 빼서, 그 다음으로 넣을 문자만 넣고, 그 문자만 업데이트 해주고,
            # 나머지 문자는 다시 넣어준다. 

            # 그런데 이렇게 하려면 문자가 두개 있어야 함. heap에 문자가 하나밖에 없다? 그러면 중복해서 못넣는다는 것이다. 
            else:

                if len(h)==1:
                    return ""

                else:
                    temp1=heapq.heappop(h)
                    temp2=heapq.heappop(h)
                    res+=temp2[1]
                    if temp2[0]+1:
                        heapq.heappush(h,[temp2[0]+1,temp2[1]])
                    heapq.heappush(h,[temp1[0],temp1[1]])
        
        return res
