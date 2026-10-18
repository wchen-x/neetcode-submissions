class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroR = set()
        zeroC = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zeroR.add(i)
                    zeroC.add(j)
                
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in zeroR or j in zeroC:
                    matrix[i][j] = 0