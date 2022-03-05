class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and "{:b}".format(n).count("1") == 1


def test_1():
    assert Solution().isPowerOfTwo(2) == True


def test_2():
    assert Solution().isPowerOfTwo(1) == True


def test_3():
    assert Solution().isPowerOfTwo(8) == True


def test_4():
    assert Solution().isPowerOfTwo(-8) == False


def test_5():
    assert Solution().isPowerOfTwo(3) == False


def test_6():
    assert Solution().isPowerOfTwo(17) == False
