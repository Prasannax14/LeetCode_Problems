class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')

        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count

        for j in range(k, len(s)):
            # Remove the left character
            if s[j - k] in vowels:
                count -= 1

            # Add the right character
            if s[j] in vowels:
                count += 1

            max_count = max(max_count, count)

            if max_count == k:
                return k

        return max_count