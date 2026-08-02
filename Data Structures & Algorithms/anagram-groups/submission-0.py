class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            characterCount = [0] * 26

            for char in s:
                characterCount[ord(char) - ord("a")] += 1
            
            result[tuple(characterCount)].append(s)

        return [[anagram for anagram in anagramGroup] for anagramGroup in result.values()]