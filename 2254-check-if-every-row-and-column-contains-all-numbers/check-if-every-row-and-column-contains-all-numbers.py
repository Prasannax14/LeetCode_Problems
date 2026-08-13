class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        # Check rows
        for i in range(n):
            seen = [0] * (n + 1)

            for j in range(n):
                a = matrix[i][j]

                if seen[a] == 1:
                    return False
                else:
                    seen[a] = 1

        # Check columns
        for i in range(n):
            seen = [0] * (n + 1)

            for j in range(n):
                a = matrix[j][i]

                if seen[a] == 1:
                    return False
                else:
                    seen[a] = 1

        return True