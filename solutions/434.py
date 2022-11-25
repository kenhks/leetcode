import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Python Built-in split
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def countSegments(self, s: str) -> int:
        return len(s.split())


class Solution2:
    """
    Iterative count
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def countSegments(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if (i == 0 or s[i - 1] == " ") and s[i] != " ":
                count += 1
        return count


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "countSegments",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("Hello, my name is John") == 5


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("Hello") == 1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(" ") == 0


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution("a  b") == 2
