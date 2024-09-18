# 11:43 시작. 83ms. 9.60% beats.
# 다른 풀이도 뭐 비슷한듯하다.

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        def convert_to_minutes(points):
            arr = points.split(":") 
            minutes = int(arr[0]) * 60 + int(arr[1])
            return minutes

        arr = [convert_to_minutes(item) for item in timePoints]
        arr.sort()
        arr.append(arr[0]+24*60)
        
        minVal = float("inf")
        for i in range(len(arr)-1):
            minVal = min(arr[i+1] - arr[i],minVal)
        
        return minVal