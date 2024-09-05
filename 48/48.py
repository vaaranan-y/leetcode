class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # 1. Transpose
        for i in range(len(matrix)):
            for j in range(i):
                temp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = temp
        
        # 2. Reverse rows
        for i in range(len(matrix)):
            matrix[i].reverse()


        