from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])

        reachesAtlantic = set()
        reachesPacific = set()

        atlanticQueue = deque()
        pacificQueue = deque()

        # Add Pacific borders
        for i in range(m):
            pacificQueue.append((0, i))
            reachesPacific.add((0, i))

        # Add Atlantic borders
        for i in range(m):
            atlanticQueue.append((n - 1, i))
            reachesAtlantic.add((n - 1, i))

        # Add left/right borders
        for i in range(n):
            pacificQueue.append((i, 0))
            reachesPacific.add((i, 0))

            atlanticQueue.append((i, m - 1))
            reachesAtlantic.add((i, m - 1))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # BFS from Atlantic
        while atlanticQueue:
            x, y = atlanticQueue.popleft()

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    if (nx, ny) not in reachesAtlantic:
                        if heights[nx][ny] >= heights[x][y]:
                            reachesAtlantic.add((nx, ny))
                            atlanticQueue.append((nx, ny))

        # BFS from Pacific
        while pacificQueue:
            x, y = pacificQueue.popleft()

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    if (nx, ny) not in reachesPacific:
                        if heights[nx][ny] >= heights[x][y]:
                            reachesPacific.add((nx, ny))
                            pacificQueue.append((nx, ny))

        return [
            [x, y]
            for x, y in reachesAtlantic
            if (x, y) in reachesPacific
        ]
