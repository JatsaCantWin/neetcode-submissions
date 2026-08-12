class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            x, y = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if x > y:
                x, y = y, x

            z = y - x
            if z > 0:
                heapq.heappush_max(stones, z)

        return 0 if len(stones) == 0 else stones[0]