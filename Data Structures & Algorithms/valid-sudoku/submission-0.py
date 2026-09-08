class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # validate row - find if there's duplicates
        for i in range(len(board)):
            s = set()
            for j in range(len(board)):
                item = board[i][j]
                if item in s:
                    return False
                elif item in '.':
                    continue
                s.add(item)


        # validate col
        for i in range(len(board)):
            s = set()
            for j in range(len(board)):
                item = board[j][i]
                if item in s:
                    return False
                elif item in '.':
                    continue
                s.add(item)

        # validate box
        starts = [
            (0,0), (0,3), (0,6),
            (3,0), (3,3), (3,6),
            (6,0), (6,3), (6,6),
        ]
        for i,j in starts:
            s = set()
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item in '.':
                        continue
                    s.add(item)


        return True