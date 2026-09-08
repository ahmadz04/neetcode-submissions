class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        num_island = 0
        visited = set()

        def dfs(i, j):
            if (i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1' or (i,j) in visited):
                return
            else:
                visited.add((i,j))
                dfs(i, j + 1)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i - 1, j)
                
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    num_island += 1
                    dfs(i, j)
        return num_island
        