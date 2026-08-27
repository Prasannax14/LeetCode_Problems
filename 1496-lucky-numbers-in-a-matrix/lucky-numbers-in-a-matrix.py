class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        result = []

        for i in range(len(matrix)):
            row_min = min(matrix[i])

            col = matrix[i].index(row_min)

            is_max = True

            for r in range(len(matrix)):
                if matrix[r][col] > row_min:
                    is_max = False
                    break

            if is_max:
                result.append(row_min)

        return result
