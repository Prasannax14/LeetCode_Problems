from math import gcd

class Solution:
    def findGCD(self, nums: list[int]) -> int:
        smallest = min(nums)
        largest = max(nums)

        return gcd(smallest, largest)