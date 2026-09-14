class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        res = []

        rows = len(matrix)
        cols = len(matrix[0])
        
        frz = False
        fcz = False
        for j in range(cols):
            if matrix[0][j] == 0:
                frz = True

        for i in range(rows):
            if matrix[i][0] == 0:
                fcz = True

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0


        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0

        if frz:
            for j in range(cols):
                matrix[0][j] = 0

        if fcz:
            for i in range(rows):
                matrix[i][0] = 0