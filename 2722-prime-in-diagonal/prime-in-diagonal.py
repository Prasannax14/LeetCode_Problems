class Solution:
    def diagonalPrime(self, nums: list[list[int]]) -> int:
        n = len(nums)
        answer = 0

        for i in range(n):
            # Main diagonal
            if self.isPrime(nums[i][i]):
                answer = max(answer, nums[i][i])

            # Other diagonal
            if self.isPrime(nums[i][n - i - 1]):
                answer = max(answer, nums[i][n - i - 1])

        return answer

    def isPrime(self, num: int) -> bool:
        if num < 2:
            return False

        i = 2

        while i * i <= num:
            if num % i == 0:
                return False
            i += 1

        return True