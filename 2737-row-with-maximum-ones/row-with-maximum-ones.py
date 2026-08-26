class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        max_ones = 0
        max_row = 0

        for i in range(len(mat)):
            count = 0

            for num in mat[i]:
                if num == 1:
                    count += 1

            if count > max_ones:
                max_ones = count
                max_row = i

        return [max_row, max_ones]
