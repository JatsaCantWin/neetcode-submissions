class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = '#' + '#'.join(s) + '#'
        n = len(s)

        p = [0] * n

        center = 0
        right = 0

        for i in range(1, n - 1):
            mirror = 2 * center - i

            if i < right:
                p[i] = min(right - i, p[mirror])

            while (
                i + p[i] + 1 < n
                and i - p[i] - 1 >= 0
                and s[i + p[i] + 1] == s[i - p[i] - 1]
            ):
                p[i] += 1

            if i + p[i] > right:
                center = i
                right = i + p[i]

        center = p.index(max(p))
        length = p[center]

        result = s[center - length : center + length + 1]

        return result.replace('#', '')
