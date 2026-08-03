class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        argumentStack = []

        for token in tokens:
            match(token):
                case '+':
                    right = argumentStack.pop()
                    left = argumentStack.pop()

                    operationResult = left + right

                    argumentStack.append(operationResult)
                case '-':
                    right = argumentStack.pop()
                    left = argumentStack.pop()

                    operationResult = left - right

                    argumentStack.append(operationResult)
                case '*':
                    right = argumentStack.pop()
                    left = argumentStack.pop()

                    operationResult = left * right

                    argumentStack.append(operationResult)
                case '/':
                    right = argumentStack.pop()
                    left = argumentStack.pop()

                    operationResult = int(left / right)
                    argumentStack.append(operationResult)
                case _:
                    argumentStack.append(int(token))
        
        return argumentStack[0]

                