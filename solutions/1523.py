class Solution:
    def countOdds(self, low: int, high: int) -> int:
        offset = 0
        if low % 2 == 1:
            offset += 1
        elif high % 2 == 1:
            offset += 1
        return offset + (high - low) // 2


def test_1():
    assert Solution().countOdds(3, 7) == 3


def test_2():
    assert Solution().countOdds(8, 10) == 1


def test_3():
    assert Solution().countOdds(8, 8) == 0


def test_4():
    assert Solution().countOdds(1, 1) == 1


def test_5():
    assert Solution().countOdds(1, 10) == 5


def test_6():
    assert Solution().countOdds(10, 15) == 3
