import itertools

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Iterative
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def countAndSay(self, n: int) -> str:
        s = "1"
        while n > 1:
            c_count = 1
            last_c = s[0]
            new_s = ""
            for c in s[1:] + " ":
                if c != last_c:
                    new_s += f"{c_count}{last_c}"
                    last_c = c
                    c_count = 1
                else:
                    c_count += 1
            s = new_s
            n -= 1
        return s


class Solution2:
    """
    Python built-in Groupby
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            new_result = ""
            for digit, group in itertools.groupby(result):
                count = len(list(group))
                new_result += f"{count}{digit}"
            result = new_result
        return result


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "countAndSay",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(1) == "1"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(4) == "1211"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(5) == "111221"


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(6) == "312211"
