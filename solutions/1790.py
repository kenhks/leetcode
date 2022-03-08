from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for i in nums:
            if i == 0:
                sign = 0
                break
            elif i < 0:
                sign = -sign
        return sign


def test_1():
    assert Solution().arraySign([-1, -2, -3, -4, 3, 2, 1]) == 1


def test_2():
    assert Solution().arraySign([1, 5, 0, 2, -3]) == 0


def test_3():
    assert Solution().arraySign([-1, 1, -1, 1, -1]) == -1
