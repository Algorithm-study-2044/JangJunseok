#3주차. 1차시도 시간초과.
#3주차. 2차시도. 15분. 문법실수였다. for문 안에서 return하면 for문 자체가 중단되잖아!!
#51ms. beats 48%.

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        moveX = [0,0,1,-1]
        moveY = [-1,1,0,0]
        start = image[sr][sc]

        def DFS(row,col):
            # 0 1이 들어감
            current = image[row][col]
            if current != start:
                return
            if current == color:
                return
            image[row][col] = color

            for i in range(4):
                nextSr = row + moveY[i]
                nextSc = col + moveX[i]

                if nextSr < 0 or nextSr > len(image) - 1:
                    continue 
                if nextSc < 0 or nextSc > len(image[nextSr])- 1:
                    continue

                DFS(nextSr, nextSc)
            
        DFS(sr,sc)
        return image