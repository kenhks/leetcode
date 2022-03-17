from functools import cache


class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        else:
            return self.climbStairs(n - 2) + self.climbStairs(n - 1)


class Solution2:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = a + b, a
        return a


def test_1():
    assert Solution().climbStairs(2) == 2


def test_2():
    assert Solution().climbStairs(3) == 3


def test_3():
    assert Solution().climbStairs(5) == 8


def test_4():
    assert Solution2().climbStairs(2) == 2


def test_5():
    assert Solution2().climbStairs(3) == 3


def test_6():
    assert Solution2().climbStairs(5) == 8
