class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "|"

        stringBoundries = []
        currentStringBoundry = -1

        for s in strs:
            currentStringBoundry += len(s)
            stringBoundries.append(currentStringBoundry)

        encodedStr = ""

        for stringBoundry in stringBoundries:
            encodedStr += str(stringBoundry)
            encodedStr += "/"
        
        encodedStr += "|"

        for s in strs:
            encodedStr += s

        return encodedStr

    def decode(self, s: str) -> List[str]:
        if s == "|":
            return []

        decodedStrings = []

        breakIndexesString, string = s.split('|', 1)

        breakIndexes = [int(indexString) for indexString in breakIndexesString.rstrip('/').split('/')]

        lastBreak = 0

        for breakIndex in breakIndexes:
            decodedStrings.append(string[lastBreak:breakIndex + 1])
            lastBreak = breakIndex + 1

        return decodedStrings
