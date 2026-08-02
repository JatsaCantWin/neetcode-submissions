class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charactersS = {}
        charactersT = {}

        for i in range(len(s)):
            if s[i] not in charactersS:
                charactersS[s[i]] = 0
            if t[i] not in charactersT:
                charactersT[t[i]] = 0
            
            charactersS[s[i]] += 1
            charactersT[t[i]] += 1
        
        for characterS in charactersS:
            if characterS not in charactersT:
                return False
            if charactersT[characterS] != charactersS[characterS]:
                return False
        
        return True