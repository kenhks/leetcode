class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l < r:
            mid = (l + r) // 2
            mid_square = mid * mid
            if mid_square <= x < mid_square + 2 * mid + 1:
                return mid
            elif mid_square < x:
                l = mid + 1
            elif mid_square > x:
                r = mid - 1
        return r


def test_1():
    assert Solution().mySqrt(4) == 2


def test_2():
    assert Solution().mySqrt(8) == 2


def test_3():
    assert Solution().mySqrt(0) == 0


def test_4():
    assert Solution().mySqrt(1) == 1


def test_5():
    assert Solution().mySqrt(2) == 1


def test_6():
    assert Solution().mySqrt(80) == 8


def test_7():
    assert Solution().mySqrt(12345) == 111
