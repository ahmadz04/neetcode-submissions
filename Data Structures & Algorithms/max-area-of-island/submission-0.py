class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        area = 0
        visited = set()
        def dfs(i, j):
            if (i < 0 or i == m or j < 0 or j == n or grid[i][j] == 0 or (i,j) in visited):
                return 0
            visited.add((i,j))
            return(1 + dfs(i+1, j) + 
                        dfs(i-1, j) + 
                        dfs(i, j+1) + 
                        dfs(i, j-1)
                )




        for i in range(m):
            for j in range(n):
                area = max(area, dfs(i, j))
        return area

        