#6주차. 1차시도. 25분. 이렇게 했는데 에러가 나는 상황임. 
# int has no attribute left. 

class Solution(object):
    def createBinaryTree(self, descriptions):
        hashmap = {}
        childs = set()
        parents = set()

        for item in descriptions:
            parents.add(item[0])
            childs.add(item[1])
            if item[0] in hashmap:
                if item[1] in hashmap:
                    cNode = hashmap[item[1]]
                else:
                    cNode = TreeNode(item[1])

                if item[2] == 1:
                    hashmap[item[0]].left = cNode
                else:
                    hashmap[item[0]].right = cNode
            else:
                if item[2] == 1:
                    hashmap[item[0]] = TreeNode(item[0],item[1])
                else:
                    hashmap[item[0]] = TreeNode(item[0],None,item[1])
    
        return hashmap[list(parents - childs)[0]]