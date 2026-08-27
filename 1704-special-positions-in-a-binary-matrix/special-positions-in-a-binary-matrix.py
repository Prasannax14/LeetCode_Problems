class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        # Count 1s in each row
        row_count = [sum(row) for row in mat]

        # Count 1s in each column
        col_count = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    col_count[j] += 1

        # Find special positions
        result = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if row_count[i] == 1 and col_count[j] == 1:
                        result += 1

        return result