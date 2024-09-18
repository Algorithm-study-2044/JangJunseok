# 10분 소요. 824ms. 37.42% beats.

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        cnt_dict = {}
        ing_dict = defaultdict(list)

        queue = deque(supplies)

        for i in range(len(recipes)):
            target = recipes[i]
            cnt_dict[target] = len(ingredients[i])
            for ing in ingredients[i]:
                ing_dict[ing].append(target)

        ans = []
        while queue:
            curr = queue.popleft()
            for target in ing_dict[curr]:
                cnt_dict[target] -= 1
                if cnt_dict[target] == 0:
                    queue.append(target)
                    ans.append(target)
        
        return ans