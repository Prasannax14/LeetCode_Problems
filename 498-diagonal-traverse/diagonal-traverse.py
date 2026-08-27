class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m = len(mat)
        n = len(mat[0])

        result = []

        for diagonal in range(m + n - 1):
            temp = []

            # Find starting row
            row = 0 if diagonal < n else diagonal - n + 1
            col = diagonal - row

            # Collect this diagonal
            while row < m and col >= 0:
                temp.append(mat[row][col])
                row += 1
                col -= 1

            # Reverse every other diagonal
            if diagonal % 2 == 0:
                temp.reverse()

            result.extend(temp)

        return result