#4주차. 다시해볼것.

class Solution(object):
    def invalidTransactions(self, transactions):
        res = []
        temp = [
            item.split(",") for item in transactions
        ]
        sorted_arr = sorted(temp,key=lambda x:(x[0],int(x[1])))

        start_idx = 0
        before = [None, 0, 0, None]
        for idx,trans in enumerate(sorted_arr):   

            if before[0] == trans[0]:
                #같은 사람인 경우.
                if int(trans[1]) - int(before[1]) > 60:
                    start_idx = idx
                else:
                    if trans[3] != before[3]:
                        for dd in sorted_arr[start_idx:idx+1]:
                            if int(trans[1]) - int(dd[1]) <= 60 and not int(dd[2]) > 1000:
                                res.append(','.join(dd))
                        start_idx = idx+1
            else:
                start_idx = idx
            
            if int(trans[2]) > 1000:
                res.append(','.join(trans)) 

            before = trans
        return res
        