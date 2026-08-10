class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i : set() for i in range(n)}
        exploredVertex = [False] * n

        result = n

        for edge in edges:
            a, b = edge[0], edge[1]

            graph[a].add(b)
            graph[b].add(a)

        def exploreVertex(i):
            nonlocal result

            exploredVertex[i] = True

            for neighbor in graph[i]:
                if exploredVertex[neighbor] == False:
                    result -= 1
                    exploreVertex(neighbor)

        for i in range(n):
            if exploredVertex[i] == True:
                continue
            
            exploreVertex(i)

        return result

            
            