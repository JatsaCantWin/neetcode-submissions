class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def fastEnough(speed):
            eatingTime = 0
            for pile in piles:
                eatingTime += math.ceil(pile / speed)
            return eatingTime <= h
        
        left = 1
        right = minEatingTime = max(piles)

        while left <= right:
            mid = (left + right) // 2
            
            isFastEnough = fastEnough(mid)
            if isFastEnough:
                minEatingTime = min(minEatingTime, mid)
                right = mid - 1
            else:
                left = mid + 1

        return minEatingTime