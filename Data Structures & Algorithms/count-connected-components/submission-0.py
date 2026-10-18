from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbours = defaultdict(list)

        for a, b in edges:
            neighbours[a].append(b)
            neighbours[b].append(a)
        
        seen = set()
        count = 0

        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)
            
            for neighbour in neighbours[node]:
                dfs(neighbour)
        
        for node in range(n):
            if node not in seen:
                count += 1
                dfs(node)

        return count