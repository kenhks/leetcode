import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashset
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for c in s:
            if c in seen:
                break
            seen.add(c)
        return c


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "repeatedCharacter",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("abccbaacz") == "c"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("abcdd") == "d"
