class Solution:
    def countSubstrings(self, s: str) -> int:
        s = '#' + '#'.join(s) + '#'
        n = len(s)
        result = 0
        radius = [0] * n
        center = right = 0

        for i in range(n):
            p = min(radius[2 * center - i], right - i) if i < right else 0
            while i - p > 0 and i + p < n and s[i + p] == s[i - p]:
                p += 1
            
            radius[i] = p
            if i + p > right:
                center, right = i, i + p
            result += (p + (i&1)) // 2
        
        return result