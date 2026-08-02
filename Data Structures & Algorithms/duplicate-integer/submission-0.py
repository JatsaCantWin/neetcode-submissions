class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        examinedNums = set()

        for num in nums:
            if num in examinedNums:
                return True
            
            examinedNums.add(num)
        
        return False