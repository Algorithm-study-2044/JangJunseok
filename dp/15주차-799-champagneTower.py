# 9:20 시작. 1차시도. 실패.
# 100000009, 33, 17에서 막힌다. 왜 그런거지??
# 왜 그런가 하면. 가에는 0.25씩 채워지는데, 중간에는 0.5씩 채워지니까.

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0]]
                
        #이러면 채워진 상태
        if dp[query_row] <= poured:
            return 1
        # 이러면 아직 이전 row 채우는 중임.
        elif dp[query_row-1] >= poured:
            return 0
        # 이전 row 다 채웠고 이제 떨어지는 중임.
        else:
            return (poured - dp[query_row-1]) * (1/(2**query_row))
            # dp[query_row] > poured
            # 이러면 아직 안채워진 상태.

# 2차시도. 풀이 참고한 풀이.

# 내 풀이랑은 어떻게 다른가?
# 나는 각 glass가 어느정도 양이 있을때 다 채워지는지를 파악하고 싶어서.
# 규칙을 찾고 그걸 각 array마다 구해준 다음에 그 규칙에 따라서 정답을 구했다.

# 두번째 row는 1+2니까 3일때 다 찰것이다..이런식으로.
# 정답 솔루션에서는, 그렇게 규칙을 찾는게 아니라, 
# 그 절차대로 그냥 프로그램에게 시킨 것이다. 얼마나 남을까요? 이런것을.
# 그러기 위해서 처음에 그냥 물을 overflow로 채워넣고, 그 다음에 이런것들을 하도록 했다.

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        arr = [poured]

        for i in range(query_row):
            newArr = [0]
            for a in arr:
                if a > 1:
                    val = (a-1) / 2
                    newArr[-1] += val
                    newArr.append(val)
                else:
                    newArr.append(0)

            arr = newArr

        res = arr[query_glass]
        if res > 1:
            return 1
        else:
            return res

# 그럼 이 풀이는 왜 안될까?
# 음수가 나올 가능성이 있어서이지 않을까 싶다.
# 특히 마지막에서, 일단 1보다 많이 있다는 가정 하에.
# 그리고 공간복잡도 측면에서 불리하다.

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        dp = [[0] * (item+1) for item in range(query_row+1)]

        dp[0][0] = poured

        for i in range(1,query_row+1):
            for j in range(0,len(dp[i])):
                if j == 0:
                    dp[i][j] = (dp[i-1][0] - 1) / 2
                elif j == len(dp[i])-1:
                    dp[i][j] = (dp[i-1][j-1] -1) / 2
                else:
                    dp[i][j] = (dp[i-1][j-1] -1) / 2 + (dp[i-1][j] -1) /2        

        if dp[query_row][query_glass] >= 1:
            return 1
        else:
            return dp[query_row][query_glass]



        