class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        return n == 1


def test_1():
    assert Solution().isHappy(19) == True


def test_2():
    assert Solution().isHappy(2) == False


def test_3():
    assert Solution().isHappy(4) == False
