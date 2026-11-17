class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
# 原地修改覆盖了原数据
        k = len(matrix)

        matrix1= [[0]*k for _ in range(k)]

        for i in range(k):
            for j in range(k):
                matrix1[j][k-1-i]=matrix[i][j]

        for i in range(k):
            for j in range(k):
                matrix[i][j]=matrix1[i][j]
        # return matrix1