class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        neededChars = [0] * 26
        chars = [0] * 26
        left = right = 0

        for char in s1:
            neededChars[ord(char) - ord('a')] += 1

        while right < m:
            length = right - left + 1
            chars[ord(s2[right]) - ord('a')] += 1

            if length > n:
                chars[ord(s2[left]) - ord('a')] -= 1
                left+=1
            
            if chars == neededChars:
                return True
            
            right += 1
        
        return False
