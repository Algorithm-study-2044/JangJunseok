# 이 테스트 케이스에 대해서 실패했음.
# [1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0]

class Solution(object):
    def threeEqualParts(self, arr):
        
        oneArr = [item for item in arr if item == 1]
        if len(oneArr) % 3 != 0:
            return [-1,-1]
        if all([item == 0 for item in arr]):
            return [0,len(arr)-1]

        one_per_item = len(oneArr) // 3
        one_count = 0
        pattern = ""
        result = []
        
        for index, item in enumerate(arr):
            if one_count >= 1:
                pattern += str(item)
            elif item == 1:
                pattern += str(item)
    
            if item == 1:
                one_count += 1

            if one_count == one_per_item:
                result.append(index)
                break

        arr_to_string = [str(item) for item in arr[result[0]+1:]]
        rest_string = "".join(arr_to_string)
        if pattern not in rest_string:
            return [-1,-1]
        findIndex = rest_string.find(pattern)
        rest_string_two = rest_string[findIndex + len(pattern):]
        if pattern not in rest_string_two:
            return [-1,-1]
        findIndex_two = rest_string_two.find(pattern)
        if findIndex_two + len(pattern) < len(rest_string_two):
            return [-1,-1]

        result.append(result[0]+findIndex+(len(pattern))+1)

        return result

        
            