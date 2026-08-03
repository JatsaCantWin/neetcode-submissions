class Solution:
    def isValid(self, s: str) -> bool:
        def getMatchingLeftBracket(rightBracket):
            if rightBracket == ")":
                return "("
            if rightBracket == "}":
                return "{"
            if rightBracket == "]":
                return "["

        def isRightBracket(bracket):
            return bracket in ["}", ")", "]"]

        bracketStack = []

        for bracket in s:
            if isRightBracket(bracket):
                if bracketStack == []:
                    return False
                if bracketStack.pop() != getMatchingLeftBracket(bracket):
                    return False
            else:
                bracketStack.append(bracket)
        
        return bracketStack == []
