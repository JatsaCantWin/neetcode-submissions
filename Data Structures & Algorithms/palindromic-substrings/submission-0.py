class Solution:
    def countSubstrings(self, s: str) -> int:
        s = '#' + '#'.join(s) + '#'
        n = len(s)
        result = 0

        for i in range(n):
            p = 0
            while i - p > 0 and i + p < n and s[i + p] == s[i - p]:
                if s[i + p] != '#':
                    result += 1
                
                p += 1
        
        return result
