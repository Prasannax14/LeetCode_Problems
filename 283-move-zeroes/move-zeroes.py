class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert_pos = 0

        # Move all non-zero elements to the front
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

        # Fill the remaining positions with zeroes
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1