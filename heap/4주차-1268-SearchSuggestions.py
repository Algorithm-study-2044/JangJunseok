#4주차. 15분. 229ms. 51% beats.

class Solution(object):

    def findMaximumThree(self,arr,keyword):
        res = [item for item in arr if item[0:len(keyword)] == keyword]
        
        if len(res) > 3:
            return res[0:3]
        else:
            return res

    def suggestedProducts(self, products, searchWord):
        res = []
        curr_keyword = ""
        sorted_project = sorted(products)

        for char in searchWord:
            curr_keyword += char
            res.append(self.findMaximumThree(sorted_project, curr_keyword))
        
        return res