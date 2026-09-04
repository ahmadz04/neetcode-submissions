class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # to keep track of lands alr visited
        visited = set() 
        # i and j are coords of the land/matrix
        def dfs(i, j):
            # Base Case, if we are out of bounds: 
                # if i >= # of rows or if j >= # of cols
                # if i or j < 0
                # if we reach water: grid[i,j] == 0
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1

            # Another base case: if island already visited
            if (i,j) in visited:
                return 0

            # Add the block to visited set
            visited.add((i,j))

            # Call dfs for the right
            perimeter = dfs(i, j + 1)
            # call dfs for the left
            perimeter += dfs(i, j - 1)
            # call dfs for up
            perimeter += dfs(i + 1, j)
            # call dfs for down
            perimeter += dfs(i - 1, j)

            return perimeter
        # Find a spot that is non zero, as in land:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i, j)
        return 0

