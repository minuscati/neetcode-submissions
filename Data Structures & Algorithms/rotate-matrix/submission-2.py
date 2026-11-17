class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
# 原地修改
        k = len(matrix)
        # reverse
        matrix.reverse()
        # transpose
        for i in range(k):
            for j in range(i+1,k):
                matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]