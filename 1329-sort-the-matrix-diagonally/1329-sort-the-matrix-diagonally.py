class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        # n = len(mat)
        # m = len(mat[0])
        d = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d[(i-j)].append(mat[i][j])
                
        for x in d:
            d[x].sort(reverse=True)
            
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = d[(i-j)].pop()
        
        return mat
        