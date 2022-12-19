import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Greedy
    Time Complexity: O(a + b)
    Space Complexity: O(1)
    """

    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = ""
        while a or b:
            if ans[-2:] == "aa":
                ans += "b"
                b -= 1
            elif ans[-2:] == "bb":
                ans += "a"
                a -= 1
            elif a > b:
                ans += "a"
                a -= 1
            else:
                ans += "b"
                b -= 1
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "strWithout3a3b",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(a=1, b=2) in set(["abb", "bab", "bba"])


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(a=4, b=1) == "aabaa"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(a=0, b=0) == ""


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(a=2, b=5) in set(["bbabbab", "bbababb"])


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution(a=1, b=3) in set(["bbab", "babb"])


@pytest.mark.parametrize("solution", solutions)
def test_6(solution):
    assert solution(a=1, b=1) in set(["ab", "ba"])


@pytest.mark.parametrize("solution", solutions)
def test_7(solution):
    assert solution(a=2, b=2) in set(["abba", "abab", "baba", "bbaa"])


@pytest.mark.parametrize("solution", solutions)
def test_8(solution):
    assert solution(a=3, b=3) in set(["aababb", "ababab", "bababa"])
