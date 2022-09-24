class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            for j in range(0, len(matrix[0])//2):
                matrix[i][j], matrix[i][len(matrix)-1-j] = matrix[i][len(matrix)-1-j], matrix[i][j]
