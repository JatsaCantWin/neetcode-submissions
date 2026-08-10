class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1 : 1, 2 : 2}

        def calculateWays(n):
            nonlocal cache

            if n not in cache:
                cache[n] = calculateWays(n - 1) + calculateWays(n - 2)
            
            return cache[n]
        
        return calculateWays(n)