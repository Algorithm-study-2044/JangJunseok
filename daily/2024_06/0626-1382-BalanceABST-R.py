# 다른 사람의 풀이 참고. 다시 풀어볼 것.

# 그냥 이거는, 모든 node.val 가져간다음에,

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr=[]

        # bst에 대해서는, 왼쪽은 항상 오른쪽보다 작으므로, inorder로 정렬하면, 오름차순으로 정렬된다.
        def inorder(root):
            if root==None: return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)

        # 1 2 3 4 이렇게 있을때,
        # root는 뭐가 와야 하나? 2가 되어야 하고
        
        # 그러니까 공평하게 나눠주자는 것이다. 어떻게? 
        # 중간값을 root로 두고, 나머지를 binary divide해서,

        # 그럼 val은 구할 수 있는데, 또 그 자식 노드의 left, right를 못구하니까.
        # 그걸 위해서 계속 재귀해주면서, 

        def BST(l, r):
            if l>r: return None
            m=(l+r)//2
            left=BST(l, m-1)
            right=BST(m+1, r)

            return TreeNode(arr[m], left, right)
        
        inorder(root)
        return BST(0, len(arr)-1)