class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = f"{x:b}"
        y = f"{y:b}"

        m = len(x)
        n = len(y)

        op = 0

        if m > n:
            y = '0' * (m - n) + y
        else:
            x = '0' * (n - m) + x

        mx = max(m, n)

        for i in range(mx):
            if x[i] != y[i]:
                op += 1

        return op