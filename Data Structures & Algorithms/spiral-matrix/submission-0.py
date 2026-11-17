class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#四个边界指针
        res = []

        top,left = 0,0
        bottom,right = len(matrix)-1, len(matrix[0])-1

        while left<=right and top<=bottom:

            # 1. left->right
            for j in range(left,right+1):
                res.append(matrix[top][j])
            top+=1

            # 2. top->bottom
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right-=1

            if top<=bottom:
            # 3. right->left
                for j in range(right,left-1,-1):
                    res.append(matrix[bottom][j])
                bottom-=1

            # 4.bottom->top
            if left<=right:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
        
        return res

