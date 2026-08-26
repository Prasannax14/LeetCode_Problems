class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split("-"))

        month_days = [31, 28, 31, 30, 31, 30,
                      31, 31, 30, 31, 30, 31]

        total = day

        # Add days from previous months
        for m in range(month - 1):
            total += month_days[m]

        # Leap year: February has 29 days
        if month > 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            total += 1

        return total
