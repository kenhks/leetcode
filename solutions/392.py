import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Two pointer
    Time Complexity: O(s + t)
    Space Complexity: O(1)
    """

    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "isSubsequence",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(s="abc", t="ahbgdc")


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution(s="axc", t="ahbgdc")


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(s="", t="ahbgdc")
