class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = right = 0
        maxLength = 0
        chars = {}

        def addChar(char):
            nonlocal maxLength

            if char not in chars:
                chars[char] = 0

            chars[char] += 1

        def removeChar(char):
            chars[char] -= 1

            if chars[char] == 0:
                chars.pop(char)

        def validChars() -> bool:
            length = right - left
            
            if length - max(chars.values()) > k:
                return False

            return True

        while right < n:
            addChar(s[right])
            right += 1

            while not validChars():
                removeChar(s[left])
                left += 1
            
            length = right - left
            maxLength = max(length, maxLength)


        return maxLength