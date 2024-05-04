#2:13 1차시도 실패. 이렇게 하면 동명이인일때 잘린다.

class Solution(object):
    def accountsMerge(self, accounts):
        # 가장 naive한 접근은 무엇일까?
        # 넣어놓고, 두번째꺼는 읻란 있는지 확인해서,
        # 없으면 새로, 아니면 기존꺼에다가 집어넣는 식으로.
        
        res = []
        email_to_name = {}
        name_to_email = {}
        
        for a in accounts:
            flag = None
            for email in a[1:]:
                if email in email_to_name:
                    flag = email_to_name[email]

            if flag == None:
                # 이렇게 하면 동명이인이 있을때 잘린다.
                name_to_email[a[0]] = a[1:]
                for email in a[1:]:
                    email_to_name[email] = a[0]
            else:
                for email in a[1:]:
                    if email not in name_to_email[flag]:
                        name_to_email[flag].append(email)
                        email_to_name[email] = a[0]
        
        
        return res
    



# 3차. 다른 사람의 풀이연구.

class UnionFind:
    def __init__(self,N):
        self.m = list(range(N))
    def union(self,child,parent):
        #하고싶은것은? child의 부모를, parent의 부모와 통일해주고 싶은것이다. 
        # 근데 이렇게만 하면 안되고, 또 child의 parent인덱스를 찾아줘야 한다? 그건 왜 그런거지.
        # 다를 수 있는 경우는, 결국 이미 이전에 child의 부모가 바뀌었을때 아니겠나.

        # 그때 그 부모까지 찾아서, 그거를 부모의 original로 교체해주어야 한다는 것이다.
        self.m[child] = self.m[self.find(parent)]
    
    def find(self,x):
        if self.m[x] != x:
            self.m[x] = self.find(self.m[x])
        # 이제 self.m[x]에는 가장 부모인 애의 index(value)가 들어가있다.
        return self.m[x]


class Solution(object):
    def accountsMerge(self, accounts):
        
        unions = UnionFind(len(accounts))

        ownership = {}
        for idx,a in enumerate(accounts):
            emails = a[1:]
            for e in emails:
                if e in ownership:
                    unions.union(idx,ownership[e])
                else:
                    ownership[e] = idx
        
        # 이러면 이제 각 idx마다 그 친구의 주인이 누구인지 알게 되었다.
        # 그 주인 idx에다가 넣어주면 된다. 어떻게?

        ans = collections.defaultdict(list)
        for email,idx in ownership.items():
            ans[unions.find(idx)].append(email)
        
        return [[accounts[idx][0]] + sorted(emails) for idx, emails in ans.items()]
                
            
