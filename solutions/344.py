from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


def test_1():
    s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(s)
    assert s == ["o", "l", "l", "e", "h"]


def test_2():
    s = ["H", "a", "n", "n", "a", "h"]
    Solution().reverseString(s)
    assert s == ["h", "a", "n", "n", "a", "H"]
