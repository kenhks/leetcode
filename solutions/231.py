class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and "{:b}".format(n).count("1") == 1


class Solution2:
    def isPowerOfTwo(self, n):
        return n and not (n & n - 1)


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


def test_7():
    assert Solution2().isPowerOfTwo(2) == True


def test_8():
    assert Solution2().isPowerOfTwo(1) == True


def test_9():
    assert Solution2().isPowerOfTwo(8) == True


def test_10():
    assert Solution2().isPowerOfTwo(-8) == False


def test_11():
    assert Solution2().isPowerOfTwo(3) == False


def test_12():
    assert Solution2().isPowerOfTwo(17) == False
