class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[]for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited=set()
        count=0
        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1
        return count
        #TIme and space is O(n+m) and O(n+m) respectively