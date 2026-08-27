class Solution:
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        top = x
        bottom = x + k - 1

        while top < bottom:
            for col in range(y, y + k):
                grid[top][col], grid[bottom][col] = (
                    grid[bottom][col],
                    grid[top][col]
                )

            top += 1
            bottom -= 1

        return grid