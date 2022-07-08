class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat
        
        new_mat = [[0 for _ in range(c)] for _ in range(r)]
        i = 0
        while i<r*c:
            new_mat[i//c][i%c] = mat[i//n][i%n]
            i+=1
            
        return new_mat