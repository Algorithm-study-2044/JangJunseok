# 11:27. 10분 소요. 769ms. 24.74% beats.

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr = customers[0][0]
        total = 0
        for cust in customers:
            if curr > cust[0]:
                total += curr - cust[0]
            else:
                curr = cust[0]    
            total += cust[1]        
            curr += cust[1]
        
        return total / len(customers)
    

# 다른 사람의 풀이.

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        available_at = 0
        total_wait = 0
        for arrival, t in customers:
            available_at = max(available_at, arrival) + t
            total_wait += available_at - arrival
        
        return total_wait / len(customers)