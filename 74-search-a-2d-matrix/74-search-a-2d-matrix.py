class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m = len(matrix)
        # n = len(matrix[0])
        # i, j = 0, n - 1
        # # for i in range(len(matrix)):
        # #     for j in range(len(matrix[i][j])):
        # while i < m and ~j:
        #     # cell == matrix[i][j]
        #     if target == matrix[i][j]:
        #         return True
        #     elif target < matrix[i][j]:
        #         j -= 1
        #     else:
        #         i += 1
        # return False
    
    
    
    
        if matrix == [] or matrix is None:
            return False
        col = len(matrix[0])-1
        row = 0
        while col>=0 and row<len(matrix):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col]>target:
                col -= 1
            else:
                row += 1
        return False