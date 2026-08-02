class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visitedVertices = set()

        if len(edges) != n - 1:
            return False

        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        queue = deque([(0, -1)])
        while queue:
            node, parent = queue.popleft()

            if node in visitedVertices:
                return False

            visitedVertices.add(node)

            for neighbor in graph[node]:
                if neighbor != parent:
                    queue.append((neighbor, node))
            
        if n != len(visitedVertices):
            return False

        return True