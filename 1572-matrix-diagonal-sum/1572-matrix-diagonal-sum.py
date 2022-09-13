class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        sum = 0
        for i in range(len(mat)):
            sum += mat[i][i]
            
        for i in range(len(mat)):
            if len(mat[i])-1-i != i:
                sum += mat[i][len(mat[i])-1-i]
        
        return sum
        