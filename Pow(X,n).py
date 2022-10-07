class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0: x = 1/x; n = -n
        def power(x, n):
            q, r = divmod(n, 2)
            if q == 0:
                return x ** r
            return x ** r * power(x, q) ** 2
        return power(x, n)