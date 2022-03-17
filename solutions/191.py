class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


class Solution2:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n = n & (n - 1)
            ans += 1
        return ans


def test_1():
    assert Solution().hammingWeight(int("00000000000000000000000000001011", 2)) == 3


def test_2():
    assert Solution().hammingWeight(int("011", 2)) == 2


def test_3():
    assert Solution().hammingWeight(int("0000000000000000000001110001011", 2)) == 6


def test_4():
    assert Solution2().hammingWeight(int("00000000000000000000000000001011", 2)) == 3


def test_5():
    assert Solution2().hammingWeight(int("011", 2)) == 2


def test_6():
    assert Solution2().hammingWeight(int("0000000000000000000001110001011", 2)) == 6
