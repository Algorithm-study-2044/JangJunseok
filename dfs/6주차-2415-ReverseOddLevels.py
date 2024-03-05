#6주차. 17분. 1101ms. 5% beats. BFS로도 풀어볼것.

class Solution(object):
    def reverseOddLevels(self, root):

        def reverseNode(a,b,depth):
            if depth % 2 == 1:
                aVal = a.val
                a.val = b.val
                b.val = aVal
            if a.left:
                reverseNode(a.left,b.right,depth+1)
                reverseNode(a.right,b.left,depth+1)
        if root.left:
            reverseNode(root.left, root.right, 1)

        return root