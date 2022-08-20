import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Sliding window
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "strStr",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("hello", "ll") == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("aaaaa", "bba") == -1
