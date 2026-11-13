class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
# 思路：展平然后二分查找
        # width = len(matrix[0])
        # height =len(matrix)
        flatten_ma = [val for row in matrix for val in row]
        left = 0
        right = len(flatten_ma)-1
        while left <= right:
            mid = (left+right)//2
            if flatten_ma[mid] == target:
                return True
            elif flatten_ma[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return False

        