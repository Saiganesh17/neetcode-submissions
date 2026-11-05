class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]

        # Build directed graph
        for i in range(n):
            x1, y1, r = bombs[i]

            for j in range(n):
                if i == j:
                    continue

                x2, y2, _ = bombs[j]

                dx = x1 - x2
                dy = y1 - y2

                if dx * dx + dy * dy <= r * r:
                    graph[i].append(j)

        # DFS to count detonated bombs
        def dfs(node, visited):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

            return len(visited)

        # Try detonating each bomb
        ans = 0

        for i in range(n):
            visited = set()
            ans = max(ans, dfs(i, visited))

        return ans
        #Time and space is O(n^3) and O(n^2) respectively