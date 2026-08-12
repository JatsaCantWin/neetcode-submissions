class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroTopRow = False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        zeroTopRow = True
                    else:
                        matrix[i][0] = 0
                    
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
            
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        
        if zeroTopRow:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0