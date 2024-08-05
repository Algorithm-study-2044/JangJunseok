# 11:42 시작. 1376ms. 12.71% beats.
# 가장 단순한 방법은, 
# 주어진 recipe중에서 만들 수 있는 것만 만들고. ans에 추가하고
# 나머지를 iterate하면서, 또 찾고,
# 만약에 하나도 못만든다? 그러면 그대로 ans를 반환하는.

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supply_set = set(supplies)
        ans = []
        made_something = True
        
        while made_something:
            made_something = False
            for i in range(len(recipes)):
                if recipes[i] in supply_set:
                    continue
                if all(ingredient in supply_set for ingredient in ingredients[i]):
                    supply_set.add(recipes[i])
                    ans.append(recipes[i])
                    made_something = True
        
        return ans
    

# 다른 방법은 없을까?
# 위상 정렬을 활용한 풀이.

from typing import List
from collections import deque, defaultdict

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Initialize the graph and in-degree count
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        
        # Build the graph
        for recipe, ingredient_list in zip(recipes, ingredients):
            for ingredient in ingredient_list:
                graph[ingredient].append(recipe)
                in_degree[recipe] += 1
        
        # Initialize the queue with supplies
        queue = deque(supplies)
        result = []
        
        # Perform topological sort
        while queue:
            current = queue.popleft()
            if current in recipes:
                result.append(current)

            # neighbor는 recipe들이다.
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result

# Example usage:
recipes = ["bread", "sandwich", "burger"]
ingredients = [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]]
supplies = ["yeast", "flour", "meat"]

sol = Solution()
print(sol.findAllRecipes(recipes, ingredients, supplies))  # Output: ["bread", "sandwich", "burger"]
