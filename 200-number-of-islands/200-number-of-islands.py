class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()
        
        def bfs(i,j):
            q = collections.deque()
            visited.add((i,j))
            q.append((i,j))
            
            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                
                for dr, dc in directions:
                    r,c = row+dr, col+dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c)) 
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j)not in visited:
                    bfs(i,j)
                    islands += 1
        return islands