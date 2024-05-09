#8:46. 20분 소요. 41ms. 50% beats.

# 1 / 2 3 / 4 5 6 7 / 8 9 10
# 그냥 그 count를 bin으로 했을때, 
# 1, 22, 333 이니까
# 오른쪽부터 넣으면서.

class Solution(object):
    def connect(self, root):
        if not root:
            return root
        
        level_dict = defaultdict(list)
        
        def BFS(node,level_dict):
            queue = deque([node])
            cnt = 0

            while queue:
                curr = queue.popleft()
                cnt += 1
                
                idx = len(bin(cnt))
                if level_dict[idx]:
                    # 만약 오른쪽이 있다면 연결해주고
                    curr.next = level_dict[idx][-1]

                level_dict[idx].append(curr)
                

                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
        
        BFS(root,level_dict)
            
        return root
                    