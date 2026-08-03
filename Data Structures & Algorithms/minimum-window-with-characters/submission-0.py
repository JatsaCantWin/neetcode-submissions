class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        result = ""
        minLength = float("inf")

        neededChars = {}

        for char in t:
            if char not in neededChars:
                neededChars[char] = 0
            neededChars[char] += 1
        
        left = right = 0

        chars = {char: 0 for char in neededChars}

        while right < n:
            if s[right] in neededChars:
                chars[s[right]] += 1
            
            valid = True
            for char in neededChars:
                if chars[char] < neededChars[char]:
                    valid = False
                    break

            if valid:
                while valid:
                    length = right - left + 1

                    if length < minLength:
                        minLength = length
                        result = s[left:right + 1]

                    if s[left] in chars:
                        chars[s[left]] -= 1

                    left += 1

                    valid = True
                    for char in neededChars:
                        if chars[char] < neededChars[char]:
                            valid = False
                            break

            right += 1

        return result