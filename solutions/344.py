from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Swap in-place
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "reverseString",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    s = ["h", "e", "l", "l", "o"]
    solution(s)
    assert s == ["o", "l", "l", "e", "h"]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    s = ["H", "a", "n", "n", "a", "h"]
    solution(s)
    assert s == ["h", "a", "n", "n", "a", "H"]
