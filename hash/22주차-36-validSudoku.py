# 9:08. 시작. 21분 소요.
# row 9개
# col 9개
# room 9개에 대한 set을 만든다.

# room 어떻게 분리할 것인지.
# 3을 기준으로. (2,2) 까지는 0,0에 들어간다. 
# (3,0)은? 
# x,y좌표를 //3 한 값을 key로 하면 된다.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        room = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                val = board[i][j]
                if val == ".":
                    continue
                coord = (i//3, j//3)
                if val in row[i] or val in col[j] or val in room[coord]:
                    return False
                row[i].add(val)
                col[j].add(val)
                room[coord].add(val)
        
        return True