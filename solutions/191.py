class Solution:
    def hammingWeight(self, n: int) -> int:
        return "{:b}".format(n).count("1")


class Solution2:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            print(n, n - 1, ans)
            n = n & (n - 1)
            ans += 1
        return ans


def test_1():
    assert Solution2().hammingWeight(int("00000000000000000000000000001011", 2)) == 3


def test_2():
    assert Solution2().hammingWeight(int("011", 2)) == 2


def test_3():
    assert Solution2().hammingWeight(int("0000000000000000000001110001011", 2)) == 6
