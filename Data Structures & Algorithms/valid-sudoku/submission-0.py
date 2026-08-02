class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudokuRows = [set() for _ in range(9)]
        sudokuColumns = [set() for _ in range(9)]
        sudokuBoxes = [set() for _ in range(9)]

        for i, row in enumerate(board):
            for j, column in enumerate(row):
                currentNumber = board[i][j]

                if currentNumber =='.':
                    continue

                box = j // 3 + (i // 3 * 3)

                if currentNumber in sudokuRows[i]:
                    return False
                if currentNumber in sudokuColumns[j]:
                    return False
                if currentNumber in sudokuBoxes[box]:
                    return False

                sudokuRows[i].add(currentNumber)
                sudokuColumns[j].add(currentNumber)
                sudokuBoxes[box].add(currentNumber)

        return True