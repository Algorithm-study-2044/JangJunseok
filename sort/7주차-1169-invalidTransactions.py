#1차시도. 실패. 다른 사람의 풀이 연구.


# 일단 hash_map을 만들어서, 해당 시간을 key로, 
class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        
        r = {}
                
        inv = []        
        for i in transactions:
            split = i.decode("utf-8").split(",")
            name = str(split[0])
            time = int(split[1])
            amount = int(split[2])
            city = str(split[3])
            
            if time not in r:
                r[time] = {
                    name: [city]
                }
            else:
                if name not in r[time]:
                    r[time][name]=[city]
                else:
                    r[time][name].append(city)
                    
        
        for i in transactions:
            split = i.decode("utf-8").split(",")
            name = str(split[0])
            time = int(split[1])
            amount = int(split[2])
            city = str(split[3])
            
            
            if amount > 1000:
                inv.append(i)
                continue
            
            for j in range(time-60, time+61):
                if j not in r:
                    continue
                if name not in r[j]:
                    continue
                # 두번째는 이해가 되는데 첫번째는 왜 그런거지? 
                # 같은 city가 여러개일수도 있지 않나? 
                # 아니다. 스캔했을때, 같은 시간대에 하나의 이름에는 하나의 도시만 있어야 한다.
                # 그렇지 않으면 invalid이다. 왜? 30분에 -> 준석이가 -> 상하이,도쿄에 있을수는 없으니까.
                
                if len(r[j][name]) > 1 or (r[j][name][0] != city):
                    inv.append(i)
                    break
                                        
        return inv       