class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        ops=0
        for j in range(n):
            for i in range(1,m):
                if(grid[i][j]<=grid[i-1][j]):
                    needed=grid[i-1][j]+1
                    ops+=needed-grid[i][j]
                    grid[i][j]=needed
        return ops
        