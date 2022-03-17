from functools import cache


class Solution:
    @cache
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)


class Solution2:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a


def test_1():
    assert Solution().fib(2) == 1


def test_2():
    assert Solution().fib(3) == 2


def test_3():
    assert Solution().fib(4) == 3


def test_4():
    assert Solution2().fib(2) == 1


def test_5():
    assert Solution2().fib(3) == 2


def test_6():
    assert Solution2().fib(4) == 3
