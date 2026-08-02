class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        indexLeft = 0
        indexRight = n - 1

        def notValidChar(char):
            char = char.lower()

            if ord(char) >= ord("a") and ord(char) <= ord("z"):
                return False
            
            if ord(char) >= ord("0") and ord(char) <= ord("9"):
                return False

            return True

        while indexLeft < indexRight:
            if notValidChar(s[indexLeft]):
                indexLeft += 1
                continue
            
            if notValidChar(s[indexRight]):
                indexRight -= 1
                continue

            if s[indexLeft].lower() != s[indexRight].lower():
                return False
            
            indexLeft += 1
            indexRight -= 1

        return True
        
